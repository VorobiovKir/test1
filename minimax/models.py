# -*- coding: utf-8 -*-
import django
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from s3direct.fields import S3DirectField
from bs4 import BeautifulSoup

from minimax.utils.model_utils import RichTextField
from minimax.utils.text_utils import truncate_chars


class PublishableContent(models.Model):
    """
    Abstract model to be used whenever hidden/published flag is required.
    """
    STATUS_HIDDEN = 'HIDDEN'
    STATUS_PUBLISHED = 'PUBLISHED'
    STATUS_CHOICES = [
        (STATUS_HIDDEN, _('Hidden')),
        (STATUS_PUBLISHED, _('Published')),
    ]

    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default=STATUS_HIDDEN, verbose_name=_(u'status')
    )

    class Meta:
        abstract = True


class RelatedDocuments(object):
    @property
    def all_related_documents(self):
        if not hasattr(self, 'pk'):
            raise AttributeError('Model object has no attribute "pk"')
        if not hasattr(self, 'type'):
            raise AttributeError('Model object has no attribute "type"')

        if isinstance(self, Technology):
            return Document.objects.filter(
                Q(technology_relation_type=Document.RELATION_TYPE_ALL) | (
                    Q(technology_relation_type=Document.RELATION_TYPE_BY_ITEM) &
                    Q(related_technologies__in=[self.pk])
                ) | (
                    Q(technology_relation_type=Document.RELATION_TYPE_BY_TYPE) &
                    Q(related_technology_types__in=[self.type.pk])
                )
            )
        return Document.objects.filter(
            Q(solution_relation_type=Document.RELATION_TYPE_ALL) | (
                Q(solution_relation_type=Document.RELATION_TYPE_BY_ITEM) &
                Q(related_solutions__in=[self.pk])
            ) | (
                Q(solution_relation_type=Document.RELATION_TYPE_BY_TYPE) &
                Q(related_solution_types__in=[self.type.pk])
            )
        )


class PageTreeItem(MPTTModel, PublishableContent):
    """
    An item to be used to build the page tree of the overall website.
    """
    TYPE_STANDARD = 'STANDARD'
    TYPE_MENU_ITEM = 'MENU_ITEM'
    TYPE_HOME = 'HOME'
    TYPE_NEWS = 'NEWS'
    TYPE_TRAINING = 'TRAININGS'
    TYPE_FAIRS = 'FAIRS'
    TYPE_PEOPLE = 'PEOPLE'
    TYPE_TECHNOLOGIES = 'TECHNOLOGIES'
    TYPE_SOLUTIONS = 'SOLUTIONS'
    TYPE_SERVICES = 'SERVICES'
    TYPE_DOWNLOADS = 'DOWNLOADS'
    TYPE_CONTACT = 'CONTACT'
    TYPE_CHOICES = [
        (TYPE_STANDARD, _(u'Standard')),
        (TYPE_MENU_ITEM, _(u'Menu item')),
        (TYPE_HOME, _(u'Home')),
        (TYPE_NEWS, _(u'News')),
        (TYPE_FAIRS, _(u'Fairs')),
        (TYPE_TRAINING, _(u'Trainings')),
        (TYPE_PEOPLE, _(u'People')),
        (TYPE_TECHNOLOGIES, _(u'Technologies')),
        (TYPE_SOLUTIONS, _(u'Solutions')),
        (TYPE_SERVICES, _(u'Services')),
        (TYPE_DOWNLOADS, _(u'Downloads')),
        (TYPE_CONTACT, _(u'Contact')),
    ]

    name = models.CharField(max_length=100)
    position = models.PositiveIntegerField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default=TYPE_STANDARD, verbose_name=_(u'type'))
    # To be used if type is MENU_ITEM, TECHNOLOGIES, SOLUTIONS, SERVICES, DOWNLOADS, CONTACTS
    title = models.CharField(max_length=255, null=True, blank=True)
    teaser = models.TextField(null=True, blank=True, verbose_name=_(u'teaser'))
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        if self.parent:
            if not self.slug and self.name:
                self.slug = slugify(self.name)
                self.save()
            return "%s%s/" % (self.parent.get_absolute_url(), self.slug)
        else:
            return "/"

    class MPTTMeta:
        order_insertion_by = ['position']

    class Meta:
        verbose_name = _(u'Navigation entry')
        verbose_name_plural = _(u'Navigation entries')


class WebPage(PublishableContent):
    """
    A web page as part of the overall website. In order to be displayed on the frontend, the web page needs to be
    linked within the page tree.
    """
    name = models.CharField(max_length=100, blank=True, null=True,
                            help_text=_(u'The name of the page used in the navigation.'))
    template = models.ForeignKey('Template', related_name='pages', null=True, blank=True)
    header_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_(u'title'))
    header_caption = models.TextField(default='', blank=True, verbose_name=_(u'caption'))
    header_image = S3DirectField(dest='page_banner', image=True, editable=True, null=True, blank=True)

    ANY_LANGUAGE_FIELDS = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        parent_menu = self.related_page_tree_items.get()
        return parent_menu.page_tree_item.get_absolute_url()

    class Meta:
        verbose_name = _(u'web page')
        verbose_name_plural = _(u'web pages')


class PageContent(models.Model):
    """
    A standard piece of page content to be used within normal, manually created web pages.
    """
    TYPE_TEXT = 'TEXT'
    TYPE_TEXT_W_IMAGE = 'TEXT_W_IMAGE'
    TYPE_TEXT_W_BGIMAGE = 'TEXT_W_BGIMAGE'
    TYPE_CHOICES = [
        (TYPE_TEXT, _(u'Text')),
        (TYPE_TEXT_W_IMAGE, _(u'Text with image')),
        (TYPE_TEXT_W_BGIMAGE, _(u'Text with background image')),
    ]
    POSITION_LEFT = 'LEFT'
    POSITION_RIGHT = 'RIGHT'
    POSITION_CHOICES = [
        (POSITION_LEFT, _(u'Left')),
        (POSITION_RIGHT, _(u'Right')),
    ]
    WIDTH_25 = 25
    WIDTH_33 = 33
    WIDTH_50 = 50
    WIDTH_CHOICES = [
        (WIDTH_25, '25%'),
        (WIDTH_33, '33%'),
        (WIDTH_50, '50%'),
    ]
    page = models.ForeignKey(WebPage, related_name='content')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default=TYPE_TEXT, verbose_name=_(u'type'))
    text = RichTextField(default='', blank=True, verbose_name=_(u'text'))
    image = S3DirectField(dest='page_content', image=True, editable=True, null=True, blank=True)
    image_position = models.CharField(max_length=15, choices=POSITION_CHOICES, default=POSITION_LEFT,
                                      verbose_name=_(u'position'), null=True, blank=True)
    image_width = models.PositiveSmallIntegerField(choices=WIDTH_CHOICES, default=WIDTH_33, verbose_name=_(u'width'),
                                                   null=True, blank=True)
    image_caption = models.CharField(max_length=255, blank=True, null=True)
    position = models.PositiveSmallIntegerField("Position", null=True, blank=True)

    def __unicode__(self):
        return truncate_chars(strip_tags(self.text), 40)

    class Meta:
        verbose_name = _(u'content element')
        verbose_name_plural = _(u'content section')
        ordering = ['position']


class Region(models.Model):
    """
    Represents a specific website instance.
    """
    ACTIVE_YES = 1
    ACTIVE_NO = 0
    ACTIVE_CHOICES = [
        (ACTIVE_YES, _('Yes')),
        (ACTIVE_NO, _('No')),
    ]
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
    default_language = models.CharField(max_length=15, choices=settings.LANGUAGES, default=settings.LANGUAGES[0])
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES, default=ACTIVE_NO)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'region')
        verbose_name_plural = _(u'regions')


class WebPageRelation(models.Model):
    """
    Class to be used when linking a web page from within the page tree.
    """
    page_tree_item = models.ForeignKey(PageTreeItem, related_name='pages')
    region = models.ForeignKey(Region)
    web_page = models.ForeignKey(WebPage, related_name='related_page_tree_items')

    class Meta:
        verbose_name = _(u'related web page')
        verbose_name_plural = _(u'related web pages')
        ordering = ['region__id']
        unique_together = ('region', 'page_tree_item')


class NewsCategory(PublishableContent):
    name = models.CharField(max_length=126)
    color = models.CharField(max_length=6)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'news category')
        verbose_name_plural = _(u'news categories')


class NewsArticle(PublishableContent):
    """
    Represents a news article as it is shown on the web page.
    """
    title = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateTimeField(default=django.utils.timezone.now)
    # [A] del teaser
    # teaser = models.TextField(null=True, blank=True, verbose_name=_(u'teaser'))
    description = RichTextField(default='', blank=True, verbose_name=_(u'description'))
    key_image = S3DirectField(dest='news', image=True, editable=True, null=True)
    category = models.ForeignKey(NewsCategory, related_name='category')
    show_on_homepage = models.BooleanField(default=True)
    expire_on_homepage = models.DateField(null=True, blank=True)

    ANY_LANGUAGE_FIELDS = ['title']

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'news article')
        verbose_name_plural = _(u'news articles')
        ordering = ['-publication_date']


# [A]
# class NewsArticleImage(models.Model):
#     """
#     The number of images (other than the key images) related to a news articles.
#     """
#     article = models.ForeignKey(NewsArticle)
#     image = S3DirectField(dest='news', image=True, editable=True)
#     position = models.PositiveSmallIntegerField()
#
#     class Meta:
#         ordering = ['position']
#         verbose_name = _(u'image')
#         verbose_name_plural = _(u'images')


class Training(PublishableContent):
    """
    A training session promoted on the website.
    """
    title = models.CharField(max_length=100, blank=True, null=True)

    ANY_LANGUAGE_FIELDS = ['title']

    # TODO: To be completed

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'training')
        verbose_name_plural = _(u'trainings')


class Fair(PublishableContent):
    """
    Fair related information as promoted on the website.
    """
    name = models.CharField(max_length=100, blank=True, null=True)

    ANY_LANGUAGE_FIELDS = ['name']

    # TODO: To be completed

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'fair')
        verbose_name_plural = _(u'fairs')


class TechnologyMapPoint(models.Model):
    """
    Map points for a technology
    """
    title = models.CharField(max_length=200, null=True, blank=True)
    image = S3DirectField(dest='technologies', image=True, editable=True, blank=True, null=True)
    position_x = models.DecimalField(max_digits=6, decimal_places=2,
                                     validators=[MinValueValidator(0), MaxValueValidator(100)])
    position_y = models.DecimalField(max_digits=6, decimal_places=2,
                                     validators=[MinValueValidator(0), MaxValueValidator(100)])
    description = RichTextField(default='', blank=True)
    technology = models.ForeignKey('Technology', related_name='map_points')

    ANY_LANGUAGE_FIELDS = ['title']

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'map point')
        verbose_name_plural = _(u'map points')


class TechnologyFunctionTab(models.Model):
    """
    Map points for a technology
    """
    title = models.CharField(max_length=200, blank=True, null=True)
    teaser = models.TextField(default='', blank=True, )
    description = RichTextField(default='', blank=True)
    technology = models.ForeignKey('Technology', related_name='function_tabs')
    position = models.PositiveSmallIntegerField(null=True, blank=True)

    ANY_LANGUAGE_FIELDS = ['title']

    class Meta:
        ordering = ['position']
        verbose_name = _(u'function tab')
        verbose_name_plural = _(u'function tabs')

    def __unicode__(self):
        return self.title


class TechnologyType(models.Model):
    """
    A type a technology item is related to.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    ANY_LANGUAGE_FIELDS = ['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            self.save()
        return "%s/" % self.slug

    class Meta:
        verbose_name = _(u'technology type')
        verbose_name_plural = _(u'technology types')


class Technology(PublishableContent, RelatedDocuments):
    """
    A technology item as it is promoted on the website.
    """
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.ForeignKey(TechnologyType, related_name='technologies')
    slug = models.SlugField(max_length=100, unique=True, null=True)

    header_text_1 = models.TextField(null=True, blank=True, verbose_name=_(u'teaser'))
    header_text_2 = models.TextField(null=True, blank=True, verbose_name=_(u'text'))
    header_image = S3DirectField(dest='page_banner', image=True, editable=True, null=True, blank=True)

    primary_description = RichTextField(default='', blank=True, verbose_name=_(u'description'))
    primary_description_image = S3DirectField(dest='technologies', image=True, editable=True, null=True, blank=True,
                                              verbose_name=_(u'image'))
    interactive_map_image = S3DirectField(dest='technologies', image=True, editable=True, null=True, blank=True)

    applications_teaser = RichTextField(default='', blank=True, verbose_name=_(u'applications'))
    referenced_applications = models.ManyToManyField('Application', blank=True)
    certifications_teaser = RichTextField(default='', blank=True, verbose_name=_(u'certifications'))
    referenced_certification_types = models.ManyToManyField('CertificationType', blank=True)
    technologies_teaser = RichTextField(default='', blank=True, verbose_name=_(u'technologies'))
    referenced_technologies = models.ManyToManyField('Technology', blank=True)

    ANY_LANGUAGE_FIELDS = ['name']

    def get_absolute_url(self):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            self.save()
        return "/technologies/%s%s/" % (self.type.get_absolute_url(), self.slug)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'technology')
        verbose_name_plural = _(u'technologies')
        ordering = ['name', ]


class SolutionType(models.Model):
    """
    A type a solution item is related to.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    ANY_LANGUAGE_FIELDS = ['name']

    def get_absolute_url(self):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            self.save()
        return "%s/" % self.slug

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'solution type')
        verbose_name_plural = _(u'solution types')


class SolutionMapPoint(models.Model):
    """
    Map points for a solution interactive map
    """
    position_x = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    position_y = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    solution = models.ForeignKey('Solution', related_name='map_points')
    application = models.ForeignKey('Application', related_name='solution_map_points')
    application_description = RichTextField(default='', blank=True)

    def __unicode__(self):
        return self.application.title

    class Meta:
        verbose_name = _(u'map point')
        verbose_name_plural = _(u'map points')


class Solution(PublishableContent, RelatedDocuments):
    """
    A solution item as it is promoted on the website.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey(SolutionType, related_name='solutions')
    slug = models.SlugField(max_length=100, unique=True, null=True)

    header_text_1 = models.TextField(null=True, blank=True, verbose_name=_(u'teaser'))
    header_text_2 = models.TextField(null=True, blank=True, verbose_name=_(u'text'))
    header_image = S3DirectField(dest='page_banner', image=True, editable=True, null=True, blank=True)

    primary_description = RichTextField(default='', blank=True, verbose_name=_(u'description'))
    primary_description_image = S3DirectField(dest='solutions', image=True, editable=True, null=True, blank=True,
                                              verbose_name=_(u'image'))
    technologies_teaser = RichTextField(default='', blank=True, verbose_name=_(u'technologies'))
    referenced_technologies = models.ManyToManyField('Technology', blank=True)
    technologies_image = S3DirectField(dest='solutions', image=True, editable=True, null=True, blank=True,
                                       verbose_name=_(u'image'))

    interactive_map_image = S3DirectField(dest='solutions', image=True, editable=True, null=True, blank=True)

    ANY_LANGUAGE_FIELDS = ['name']

    def get_absolute_url(self):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            self.save()
        return "/solutions/%s%s/" % (self.type.get_absolute_url(), self.slug)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'solution')
        verbose_name_plural = _(u'solutions')
        ordering = ['name', ]


class ServiceType(models.Model):
    """
    A type a service item is related to.
    """
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    ANY_LANGUAGE_FIELDS = ['name']

    def get_absolute_url(self):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            self.save()
        return "%s/" % self.slug

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'service type')
        verbose_name_plural = _(u'service types')


class Service(PublishableContent):
    """
    A service item as it is promoted on the website.
    """
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.ForeignKey(ServiceType, related_name='services')
    slug = models.SlugField(max_length=100, unique=True, null=True)

    header_text_1 = models.TextField(null=True, blank=True, verbose_name=_(u'teaser'))
    header_text_2 = models.TextField(null=True, blank=True, verbose_name=_(u'text'))
    header_image = S3DirectField(dest='page_banner', image=True, editable=True, null=True, blank=True)

    description_title = models.CharField(max_length=100, blank=True, null=True)
    description_left = RichTextField(default='', blank=True, verbose_name=_(u'description left column'))
    description_left_image = S3DirectField(dest='solutions', image=True, editable=True, null=True, blank=True,
                                           verbose_name=_(u'image left column'))
    description_left_image_title = models.CharField(default='', max_length=100, blank=True, null=True,
                                                    verbose_name=_('image title'))
    description_right = RichTextField(default='', blank=True, verbose_name=_(u'description right column'),
                                      help_text=_('if left blank, the description will be rendered on one column'))
    description_right_image = S3DirectField(dest='solutions', image=True, editable=True, null=True, blank=True,
                                            verbose_name=_(u'image right column'))
    description_right_image_title = models.CharField(default='', max_length=100, blank=True, null=True,
                                                     verbose_name=_('image title'))
    details_text = RichTextField(default='', blank=True, verbose_name=_(u'scope in details'))
    details_image = S3DirectField(dest='solutions', image=True, editable=True, null=True, blank=True, verbose_name=_(u'details image'))

    ANY_LANGUAGE_FIELDS = ['name']

    def get_absolute_url(self):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            self.save()
        return "/services/%s%s/" % (self.type.get_absolute_url(), self.slug)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'service')
        verbose_name_plural = _(u'services')
        ordering = ['name', ]

    # We need to beautify some tags
    def save(self, *args, **kwargs):
        # We need to update the list check marks for all languages.
        for lang in settings.LANGUAGES:
            field_name = "details_text_%s" % lang[0]
            field_value = getattr(self, field_name, None)
            if field_value:
                soup = BeautifulSoup(field_value)
                if soup.ul:
                    soup.ul['class'] = 'square-items'
                    setattr(self, field_name, soup.prettify())
        super(Service, self).save(*args, **kwargs)


class Template(models.Model):
    """
    Page template used for page rendering.
    """
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=255, help_text='Full path without leading slash.')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'template')
        verbose_name_plural = _(u'templates')


class Employee(PublishableContent):
    """
     A person as it is represented via the 'PEOPLE' page.
    """
    name = models.CharField(max_length=50)
    responsibility = models.CharField(max_length=50, blank=True, null=True)
    quotation = models.CharField(max_length=255, blank=True, null=True)
    text = RichTextField(default='', blank=True, verbose_name=_(u'description'))
    image = S3DirectField(dest='employees', image=True, editable=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'employee')
        verbose_name_plural = _(u'employees')


class Application(PublishableContent):
    """
    Applications that can be linked to Technologies.
    """
    title = models.CharField(max_length=200, blank=True, null=True)
    image = S3DirectField(dest='applications', image=True, editable=True)

    ANY_LANGUAGE_FIELDS = ['title']

    def __unicode__(self):
        return self.title


class CertificationType(PublishableContent):
    """
    A CertificationType being held for a specific Technology, or other objects.
    """
    title = models.CharField(max_length=200, null=True, blank=True)
    image = S3DirectField(dest='certification_types', image=True, editable=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name=_(u'description'))

    ANY_LANGUAGE_FIELDS = ['title']

    def __unicode__(self):
        return self.title


class DocumentType(models.Model):
    """
    Types of documents. We can use them in filtering, maybe logo/symbol display, etc.
    """
    name = models.CharField(max_length=200, null=True, blank=True)

    ANY_LANGUAGE_FIELDS = ['name']

    def __unicode__(self):
        return self.name


class Document(PublishableContent):
    """
    Documents that can be attached to Technologies or other classes, or that can be downloaded.
    """
    RELATION_TYPE_ALL = 'A'
    RELATION_TYPE_BY_TYPE = 'T'
    RELATION_TYPE_BY_ITEM = 'I'
    RELATION_TYPE_CHOICES = [
        (RELATION_TYPE_ALL, _(u'All')),
        (RELATION_TYPE_BY_TYPE, _(u'By type')),
        (RELATION_TYPE_BY_ITEM, _(u'By item')),
    ]
    title = models.CharField(max_length=200, blank=True, null=True)
    type = models.ForeignKey(DocumentType)

    file = S3DirectField(dest='documents')
    thumbnail = models.FileField(max_length=150, upload_to='documents', blank=True, null=True)

    technology_relation_type = models.CharField(max_length=15, choices=RELATION_TYPE_CHOICES, default=RELATION_TYPE_BY_ITEM, verbose_name=_(u'Type'))
    related_technologies = models.ManyToManyField(Technology, related_name='documents', blank=True)
    related_technology_types = models.ManyToManyField(TechnologyType, related_name='documents', blank=True)

    solution_relation_type = models.CharField(max_length=15, choices=RELATION_TYPE_CHOICES, default=RELATION_TYPE_BY_ITEM, verbose_name=_(u'Type'))
    related_solutions = models.ManyToManyField(Solution, related_name='documents', blank=True)
    related_solution_types = models.ManyToManyField(SolutionType, related_name='documents', blank=True)

    ANY_LANGUAGE_FIELDS = ['title', 'file']

    def __unicode__(self):
        return self.title


class Customer(PublishableContent):
    """
    Customers of Minimax.
    """
    name = models.CharField(max_length=200)
    logo = S3DirectField(dest='customers', image=True, editable=True, null=True, blank=True)

    related_technologies = models.ManyToManyField(Technology, related_name='customers', blank=True)
    related_solutions = models.ManyToManyField(Solution, related_name='customers', blank=True)
    related_services = models.ManyToManyField(Service, related_name='customers', blank=True)

    def __unicode__(self):
        return self.name


class ExtinguishingAgent(models.Model):
    """
    Type of material that is used in extinguishing devices, like Nitrogen, Argon, etc.
    """
    name = models.CharField(max_length=100, null=True, blank=True)

    ANY_LANGUAGE_FIELDS = ['name']

    def __unicode__(self):
        return self.name


class Project(PublishableContent):
    """
    Projects are related to technologies, applications, solutions and displayed as a table at the bottom
    of the detail pages.
    """
    referenced_technologies = models.ManyToManyField(Technology, related_name='projects', blank=True)
    referenced_applications = models.ManyToManyField(Application, related_name='projects', blank=True)
    referenced_solutions = models.ManyToManyField(Solution, related_name='projects', blank=True)
    characteristics = models.CharField(max_length=255, null=True, blank=True)
    agent = models.ForeignKey(ExtinguishingAgent, blank=True, null=True)

    ANY_LANGUAGE_FIELDS = ['characteristics']

    def __unicode__(self):
        return ", ".join([a.name for a in self.referenced_technologies.all()])

    @property
    def get_technologies(self):
        return ", ".join(tech.name for tech in self.referenced_technologies.
                         filter(status=PublishableContent.STATUS_PUBLISHED))

    @property
    def get_applications(self):
        return ", ".join(application.title for application in self.referenced_applications.
                         filter(status=PublishableContent.STATUS_PUBLISHED))

    @property
    def get_solutions(self):
        return ", ".join(solution.name for solution in self.referenced_solutions.
                         filter(status=PublishableContent.STATUS_PUBLISHED))
