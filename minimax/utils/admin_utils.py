# -*- coding: utf-8 -*-
from django.utils import translation
from django.utils.html import format_html
from django.utils.translation import ugettext as _
from django import forms
from django.forms.fields import CharField
from django.core.exceptions import ValidationError
from django.conf import settings

from minimax.models import WebPage, PageTreeItem
from minimax.utils.model_utils import RichTextField
from minimax.widgets import AdminRichTextareaWidget


class CommonAdminConfigurationMixin(object):
    """
    Mixin providing some defaults configuration for standard admin views.
    """
    formfield_overrides = {
        RichTextField: {'widget': AdminRichTextareaWidget},
        # TODO: Fix this once it becomes necessary
        # ColorField: {'widget': ColorPickerWidget},
        # models.ImageField: {'widget': AdminThumbnailWidget},
        # EncryptedCharField: {'widget': PasswordInput(render_value=True)},
    }
    field_rows = {}
    readonly_fields_after_add = ()

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(CommonAdminConfigurationMixin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in self.field_rows:
            field.widget.attrs['rows'] = self.field_rows[db_field.name]
        return field

    def get_readonly_fields(self, request, obj=None):
        fields = list(super(CommonAdminConfigurationMixin, self).get_readonly_fields(request, obj=obj))
        if obj:
            fields.extend(self.readonly_fields_after_add)
        return fields


class CommonInlineConfigurationMixin(CommonAdminConfigurationMixin):
    """
    Extended version of the CommonAdminConfigurationMixin for inlines.
    """
    extra = 0


def mixin_read_only_after_add(fields):
    """
    Mixin to be used when indicating that a fields should be marked as read-only once the instance has been created.
    """

    def decorator(klass):
        def get_readonly_fields(self, request, obj=None):
            if obj:  # editing an existing object
                return self.readonly_fields + tuple(fields)
            return self.readonly_fields

        return type(klass.__name__, (klass,), dict(
            get_readonly_fields=get_readonly_fields,
        ))

    return decorator


class StyledStatusLabelMixin(object):
    """
    Generic mixin to be used where the status fields shall be rendered including proper styling.
    """

    def styled_status_label(self, obj):
        return format_html(
            '<div class="status-{0}">{1}</div>', obj.status.lower().replace('_', '-'), obj.get_status_display())

    styled_status_label.allow_tags = True
    styled_status_label.short_description = _(u'Status')
    styled_status_label.admin_order_field = 'status'


class StyledTranslatedStatusLabelMixin(object):
    """
    Generic mixin to be used where the status fields shall be rendered including proper styling.
    """

    def styled_status_label(self, obj):
        status_container = ''
        for code, language in settings.LANGUAGES:
            with translation.override(code):
                status_container += '<div class="status-{0} translated-status">{1}</div>'.format(obj.status.lower().replace('_', '-'), code.upper())
        return format_html(status_container)

    styled_status_label.allow_tags = True
    styled_status_label.short_description = _(u'Status')
    styled_status_label.admin_order_field = 'status'


class GenericRegionColumn:
    """
    The class to be used within the page tree item list view to render all region specific columns
    """

    def __init__(self, region, language):
        self.region = region
        self.language = language
        self.allow_tags = True
        self.short_description = format_html('<label class="i18n-field-label i18n-field-label-{0}">{1}</label>'.format(language, region.code))

    def __call__(self, obj):
        if obj.type == PageTreeItem.TYPE_STANDARD:
            for page in obj.pages.all():
                if page.region.id == self.region.id:
                    with translation.override(self.language):
                        return self.generate_label(page.web_page.status, self.language.upper())
                if page.region.code == 'GL':  # TODO: Replace static 'GL' label by settings variable
                    with translation.override(self.language):
                        if page.web_page.status == WebPage.STATUS_PUBLISHED:
                            return self.generate_label('overlayed', self.language.upper())
                        return self.generate_label(page.web_page.status, self.language.upper())
            return self.generate_label('error', self.language.upper())
        return self.generate_label('overlayed', self.language.upper())

    def generate_label(self, status, label):
        return format_html(
            '<div class="status-{0}">{1}</div>', status.lower().replace('_', '-'), label)

    def __unicode__(self):
        return 'region'  # To be used for the CSS class generation of the column


class AnyLanguageCharField(CharField):
    def validate(self, value):
        if value in self.empty_values and self.required:
            raise ValidationError(self.error_messages['required'], code='required')


class InteractiveMapPositionSelect(object):
    readonly_fields = ('map_position_button', )
    class Media:
        js = ('minimax/jscripts/map_position.js', )
        css = {
            'all': (
                'minimax/css/map_modal.css',
            )
        }

    def map_position_button(self, obj):
        return '<a class="image-select-point" onclick="getImagePointSelector(this, \'#id_interactive_map_image\')">' + \
               _(u'Select position on map') + '</a>'
    map_position_button.func_name = ''
    map_position_button.allow_tags = True


class AnyLanguageValidationForm(forms.ModelForm):
    def clean(self):
        error_messages = {}
        cleaned_data = super(AnyLanguageValidationForm, self).clean()
        for field in getattr(self.instance, 'ANY_LANGUAGE_FIELDS', []):
            value_found = False
            for language in settings.LANGUAGES:
                _field_name = "%s_%s" % (field, language[0])
                if cleaned_data.get(_field_name):  # model_instance.__dict__[_field_name]:
                    value_found = True
            if not value_found:
                for language in settings.LANGUAGES:
                    _field_name = "%s_%s" % (field, language[0])
                    error_messages[_field_name] = _("One of the translations has to be filled in.")
        if len(error_messages) > 0:
            raise ValidationError(error_messages)
        return cleaned_data
