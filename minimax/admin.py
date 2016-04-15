# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils import translation
from django.utils.translation import ugettext as _
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from mptt.admin import MPTTModelAdmin
from reversion.admin import VersionAdmin

from minimax.utils.admin_utils import StyledStatusLabelMixin, mixin_read_only_after_add, GenericRegionColumn, \
    CommonInlineConfigurationMixin, CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, \
    AnyLanguageValidationForm, InteractiveMapPositionSelect
from models import WebPage, PageTreeItem, Region, WebPageRelation, Training, Fair, NewsArticle, Technology, \
    TechnologyType, SolutionType, Solution, Service, ServiceType, PageContent, Template, Employee, \
    Application, CertificationType, DocumentType, Document, Customer, ExtinguishingAgent, \
    Project, TechnologyMapPoint, TechnologyFunctionTab, SolutionMapPoint, NewsCategory


class SolutionMapPointInline(InteractiveMapPositionSelect, CommonInlineConfigurationMixin, TranslationStackedInline):
    model = SolutionMapPoint
    fields = ['application', 'application_description', ('position_x', 'position_y', 'map_position_button')]
    classes = ('grp-collapse', 'grp-open',)


class TechnologyMapPointInline(InteractiveMapPositionSelect, CommonInlineConfigurationMixin, TranslationStackedInline):
    model = TechnologyMapPoint
    fields = ['title', 'description', 'image', ('position_x', 'position_y', 'map_position_button')]
    classes = ('grp-collapse', 'grp-open',)
    form = AnyLanguageValidationForm


class TechnologyFunctionTabInline(CommonInlineConfigurationMixin, TranslationStackedInline):
    model = TechnologyFunctionTab
    form = AnyLanguageValidationForm
    classes = ('grp-collapse', 'grp-open',)
    sortable_field_name = 'position'

    field_rows = {
        'teaser': 1,
    }


class WebPageRelationInline(CommonInlineConfigurationMixin, admin.TabularInline):
    form = AnyLanguageValidationForm
    model = WebPageRelation
    classes = ('grp-collapse', 'grp-open',)


# [A]
# class NewsArticleImageInline(CommonInlineConfigurationMixin, admin.TabularInline):
#     model = NewsArticleImage
#     fields = ['image', 'position']
#     classes = ('grp-collapse', 'grp-open', 'mtg-float-right',)
#     sortable_field_name = 'position'


class PageContentInlineForm(forms.ModelForm):
    def clean(self):
        type = self.cleaned_data.get('type')
        error_messages = {}
        if type == 'TEXT_W_IMAGE':
            image_position = self.cleaned_data.get('image_position')
            if not image_position:
                error_messages["image_position"] = _("Image position must not be empty")
            image_width = self.cleaned_data.get('image_width')
            if not image_width:
                error_messages["image_width"] = _("Image width must not be empty")

            if len(error_messages) > 0:
                raise ValidationError(error_messages)

        return self.cleaned_data


class PageContentInline(CommonInlineConfigurationMixin, TranslationStackedInline):
    model = PageContent
    form = PageContentInlineForm
    sortable_field_name = "position"
    fieldsets = [
        (None, {
            'fields': ['page', 'type', 'text', 'image', 'image_position', 'image_width', 'image_caption', 'position'],
            'classes': ('page-content',),
        })
    ]
    classes = ('page-content-group',)

    class Media:
        js = (
            'minimax/jscripts/show_hide_page_content_fields.js',
        )


# Normal view

@admin.register(WebPage)
class WebPageAdmin(CommonInlineConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status'],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['name'],
        }),
        (_(u'Banner section'), {
            'fields': ['header_title', 'header_caption', 'header_image'],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        (_(u'Advanced'), {
            'fields': ['template'],
            'classes': ('mtg-float-right', 'grp-collapse', 'grp-closed'),
        }),
    ]
    list_display = ['name', 'styled_status_label']
    inlines = [PageContentInline]
    search_fields = ['name']
    field_rows = {
        'header_caption': 4,
    }
    form = AnyLanguageValidationForm


@admin.register(PageTreeItem)
@mixin_read_only_after_add(['type'])
class PageTreeItemAdmin(CommonAdminConfigurationMixin, StyledStatusLabelMixin, MPTTModelAdmin, TranslationAdmin):
    actions = None  # Do not allow deletion on list view
    default_fieldsets = [
        (None, {
            'fields': ['type'],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['status', 'position'],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['parent', 'name', 'slug']
        }),

    ]
    menu_item_fieldsets = [
        (None, {
            'fields': ['type'],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['status', 'position'],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['parent', 'name', 'slug']
        }),
        (None, {
            'fields': ['title', 'teaser']
        }),
    ]
    list_display = ['name', 'styled_status_label', 'type']
    list_filter = ['type', 'parent']
    search_fields = ['name']
    inlines = []
    prepopulated_fields = {"slug": ("name",)}

    def get_form(self, request, obj=None, **kwargs):
        self.fieldsets = self.default_fieldsets
        self.inlines = []
        if obj is not None:
            if obj.type == PageTreeItem.TYPE_STANDARD:
                self.fieldsets = self.default_fieldsets
                self.inlines = [WebPageRelationInline]
            if obj.type in [PageTreeItem.TYPE_CONTACT, PageTreeItem.TYPE_DOWNLOADS, PageTreeItem.TYPE_MENU_ITEM,
                            PageTreeItem.TYPE_TECHNOLOGIES, PageTreeItem.TYPE_SOLUTIONS, PageTreeItem.TYPE_SERVICES]:
                self.fieldsets = self.menu_item_fieldsets
                self.inlines = []
        return super(MPTTModelAdmin, self).get_form(request, obj, **kwargs)

    def get_list_display(self, request):
        list = ['name', 'styled_status_label', 'type']
        for region in Region.objects.all().order_by('id'):
            for language in settings.LANGUAGES:
                with translation.override(language[0]):
                    if region.active:
                        list.append(GenericRegionColumn(region, language[0]))
        return list


@admin.register(Region)
@mixin_read_only_after_add(['code'])
class RegionAdmin(VersionAdmin, TranslationAdmin):
    actions = None  # Do not allow deletion on list view
    fieldsets = [
        (None, {
            'fields': ['default_language', 'active'],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['code', 'name']
        }),

    ]
    list_display = ['code', 'name_en', 'active_en', 'active_de']
    search_fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return False  # Do not allow deletion for now


@admin.register(NewsCategory)
class NewsCategoryAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'color']
        })
    ]


@admin.register(NewsArticle)
class NewsArticleAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status', 'key_image'],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['title']
        }),
        #
        # (None, {
        #     'fields': ['teaser', 'description']
        # }),
        (None, {
            'fields': ['description']
        }),
        (None, {
            'fields': ['category']
        }),
        (None, {
            'fields': ['show_on_homepage', 'expire_on_homepage']
        })

    ]
    list_display = ['title', 'styled_status_label']
    search_fields = ['title']
    # [A]
    # inlines = [NewsArticleImageInline]
    # [A]
    # field_rows = {
    #     'teaser': 4
    # }
    form = AnyLanguageValidationForm


@admin.register(Employee)
class EmployeeAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status', 'image'],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['name']
        }),
        (None, {
            'fields': ['responsibility', 'quotation', 'text']
        }),

    ]
    list_display = ['name', 'styled_status_label']
    search_fields = ['name']
    field_rows = {
        'text': 40
    }


@admin.register(Training)
class TrainingAdmin(StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    list_display = ['title', 'styled_status_label']
    search_fields = ['title']
    form = AnyLanguageValidationForm


@admin.register(Fair)
class FairAdmin(StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    list_display = ['name', 'styled_status_label']
    search_fields = ['name']
    form = AnyLanguageValidationForm


@admin.register(Technology)
class TechnologyAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status', 'type'],
            'classes': ('mtg-float-right',),
        }),
        (_(u'Advanced'), {
            'fields': ['slug'],
            'classes': ('mtg-float-right', 'grp-collapse', 'grp-closed'),
        }),
        (None, {
            'fields': ['name']
        }),
        (_(u'Banner section'), {
            'fields': ['header_text_1', 'header_text_2', 'header_image'],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        (_(u'Advantage overview'), {
            'fields': ['primary_description', 'primary_description_image', ],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        (_(u'Overview interactive map'), {
            'fields': ['interactive_map_image'],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        (_(u'Interactive map points'), {
            "classes": ("placeholder map_points-group",),
            "fields": ()
        }),
        (_(u'Technologies'), {
            "classes": ("placeholder function_tabs-group",),
            "fields": ()}
         ),
        (_(u'Applications'), {
            'fields': ['applications_teaser', 'referenced_applications', ],
            'classes': ('grp-collapse', 'grp-open')
        }),
        (_(u'Certifications'), {
            'fields': ['certifications_teaser', 'referenced_certification_types', ],
            'classes': ('grp-collapse', 'grp-open')
        }),
        (_(u'Related technologies that might be interesting as well'), {
            'fields': ['technologies_teaser', 'referenced_technologies', ],
            'classes': ('grp-collapse', 'grp-open')
        }),
    ]
    filter_horizontal = ['referenced_applications', 'referenced_certification_types',
                         'referenced_technologies']
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'styled_status_label', 'type']
    list_filter = ['type']
    search_fields = ['name']
    inlines = [TechnologyMapPointInline, TechnologyFunctionTabInline]
    field_rows = {
        'header_text_1': 3,
        'header_text_2': 3
    }
    form = AnyLanguageValidationForm


@admin.register(TechnologyType)
class TechnologyTypeAdmin(StyledStatusLabelMixin, VersionAdmin, TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug']
    search_fields = ['name']
    form = AnyLanguageValidationForm


@admin.register(Solution)
class SolutionAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status', 'type'],
            'classes': ('mtg-float-right',),
        }),
        (_(u'Advanced'), {
            'fields': ['slug'],
            'classes': ('mtg-float-right', 'grp-collapse', 'grp-closed'),
        }),
        (None, {
            'fields': ['name']
        }),
        (_(u'Banner section'), {
            'fields': ['header_text_1', 'header_text_2', 'header_image'],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        (_(u'Main description'), {
            'fields': ['primary_description', 'primary_description_image', ],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        (_(u'Related technologies'), {
            'fields': ['technologies_teaser', 'referenced_technologies', 'technologies_image'],
            'classes': ('grp-collapse', 'grp-open')
        }),
        (_(u'Overview interactive map'), {
            'fields': ['interactive_map_image'],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        (_(u'Interactive map points'), {
            "classes": ("placeholder map_points-group",),
            "fields": ()
        }),
    ]
    filter_horizontal = ['referenced_technologies']
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'styled_status_label', 'type']
    list_filter = ['type']
    search_fields = ['name']
    inlines = [SolutionMapPointInline, ]
    field_rows = {
        'header_text_1': 3,
        'header_text_2': 3,
    }
    form = AnyLanguageValidationForm


@admin.register(SolutionType)
class SolutionTypeAdmin(StyledStatusLabelMixin, VersionAdmin, TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug']
    search_fields = ['name']
    form = AnyLanguageValidationForm


@admin.register(Service)
class ServiceAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status', 'type'],
            'classes': ('mtg-float-right',),
        }),
        (_(u'Advanced'), {
            'fields': ['slug'],
            'classes': ('mtg-float-right', 'grp-collapse', 'grp-closed'),
        }),
        (None, {
            'fields': ['name']
        }),
        (_(u'Banner section'), {
            'fields': ['header_text_1', 'header_text_2', 'header_image'],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        (_(u'Main description'), {
            'fields': ['description_title',
                       'description_left', ('description_left_image', 'description_left_image_title'),
                       'description_right', ('description_right_image', 'description_right_image_title')],
            'classes': ('grp-collapse', 'grp-open'),
        }),
        (_(u'Scope in details'), {
            'fields': ['details_text', 'details_image'],
            'classes': ('grp-collapse', 'grp-open'),
        }),

    ]
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'styled_status_label', 'type']
    list_filter = ['type']
    search_fields = ['name']
    field_rows = {
        'header_text_1': 3,
        'header_text_2': 3,
        'primary_description_left': 3,
        'primary_description_right': 3,
        'details_text': 3
    }
    form = AnyLanguageValidationForm


@admin.register(ServiceType)
class ServiceTypeAdmin(StyledStatusLabelMixin, VersionAdmin, TranslationAdmin):
    list_display = ['name']
    search_fields = ['name']
    form = AnyLanguageValidationForm


# Overwrite Django's default site title of the admin interface.
def index(self, *args, **kwargs):
    return admin.site.__class__.index(
        self, extra_context={'title': _(u'Minimax Website Dashboard')}, *args, **kwargs)  # @UndefinedVariable


@admin.register(Template)
class TemplateAdmin(VersionAdmin):
    list_display = ['name', 'path']


@admin.register(Application)
class ApplicationAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status', ],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['title', 'image']
        }),
    ]
    list_display = ['title', 'styled_status_label']
    form = AnyLanguageValidationForm


@admin.register(CertificationType)
class CertificationTypeAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status'],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['title', 'image', 'description']
        }),
    ]

    list_display = ['title', 'styled_status_label']
    field_rows = {
        'description': 2,
    }
    form = AnyLanguageValidationForm


@admin.register(DocumentType)
class DocumentTypeAdmin(CommonAdminConfigurationMixin, TranslationAdmin):
    list_display = ['name', ]
    form = AnyLanguageValidationForm


@admin.register(Document)
class DocumentAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status', 'type', ],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['title', 'file']
        }),
        (_(u'Referenced technologies'), {
            'fields': ['technology_relation_type', 'related_technology_types', 'related_technologies'],
            'classes': ('grp-collapse', 'grp-closed'),
        }),
        (_(u'Referenced solutions'), {
            'fields': ['solution_relation_type', 'related_solution_types', 'related_solutions'],
            'classes': ('grp-collapse', 'grp-closed'),
        }),

    ]
    list_display = ['title', 'styled_status_label', 'type']
    filter_horizontal = ['related_technologies', 'related_solutions', 'related_solution_types', 'related_technology_types']
    form = AnyLanguageValidationForm

    class Media:
        js = (
            'minimax/jscripts/show_hide_document_detail_fields.js',
        )


@admin.register(Customer)
class CustomerAdmin(CommonAdminConfigurationMixin, StyledStatusLabelMixin, VersionAdmin):
    fieldsets = [
        (None, {
            'fields': ['status', 'logo', ],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['name']
        }),
        (None, {
            'fields': ['related_technologies', 'related_solutions', 'related_services']
        }),
    ]
    list_display = ['name', 'styled_status_label']
    filter_horizontal = ['related_technologies', 'related_solutions', 'related_services']
    form = AnyLanguageValidationForm


@admin.register(ExtinguishingAgent)
class ExtinguishingAgentAdmin(CommonAdminConfigurationMixin, TranslationAdmin):
    list_display = ['name', ]
    form = AnyLanguageValidationForm


@admin.register(Project)
class ProjectAdmin(CommonAdminConfigurationMixin, StyledTranslatedStatusLabelMixin, VersionAdmin, TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['status', ],
            'classes': ('mtg-float-right',),
        }),
        (None, {
            'fields': ['characteristics', 'agent']
        }),
        (None, {
            'fields': ['referenced_technologies', 'referenced_solutions', 'referenced_applications']
        }),
    ]
    list_display = ['characteristics', 'styled_status_label']
    filter_horizontal = ['referenced_technologies', 'referenced_solutions', 'referenced_applications']
    form = AnyLanguageValidationForm

admin.site.index = index.__get__(admin.site, admin.site.__class__)
