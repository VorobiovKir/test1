# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from models import WebPage, Region, Training, Fair, NewsArticle, Technology, TechnologyType, SolutionType, Solution, \
    ServiceType, Service, PageContent, PageTreeItem, Employee, Application, CertificationType, DocumentType, Document,\
    ExtinguishingAgent, Project, TechnologyMapPoint, TechnologyFunctionTab, SolutionMapPoint, NewsCategory


class PageTreeItemTranslationOptions(TranslationOptions):
    fields = ('title', 'teaser')


class WebPageTranslationOptions(TranslationOptions):
    fields = ('name', 'header_title', 'header_caption', 'status')
    fallback_undefined = {'status': None}


class PageContentTranslationOptions(TranslationOptions):
    fields = ('text', 'image_caption')


class RegionTranslationOptions(TranslationOptions):
    fields = ('name', 'active')
    fallback_undefined = {'active': None}


class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class NewsArticleTranslationOptions(TranslationOptions):
    # [A] fields = ('title', 'teaser', 'description', 'status')
    fields = ('title', 'description', 'status')
    fallback_undefined = {'status': None}


class TrainingTranslationOptions(TranslationOptions):
    fields = ('title', 'status')
    fallback_undefined = {'status': None}


class FairTranslationOptions(TranslationOptions):
    fields = ('name', 'status')
    fallback_undefined = {'status': None}


class TechnologyMapPointTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class TechnologyFunctionTabTranslationOptions(TranslationOptions):
    fields = ('title', 'teaser', 'description')


class TechnologyTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class TechnologyTranslationOptions(TranslationOptions):
    fields = ('name', 'status', 'header_text_1', 'header_text_2',
              'primary_description', 'applications_teaser', 'certifications_teaser', 'technologies_teaser')
    fallback_undefined = {'status': None}


class SolutionTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class SolutionMapPointTranslationOptions(TranslationOptions):
    fields = ('application_description', )


class SolutionTranslationOptions(TranslationOptions):
    fields = ('name', 'status', 'header_text_1', 'header_text_2', 'primary_description',
              'technologies_teaser')
    fallback_undefined = {'status': None}


class ServiceTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'status', 'header_text_1', 'header_text_2',
              'description_title', 'description_left', 'description_left_image_title',
              'description_right', 'description_right_image_title', 'details_text')
    fallback_undefined = {'status': None}


class EmployeeTranslationOptions(TranslationOptions):
    fields = ('status', 'responsibility', 'quotation', 'text')
    fallback_undefined = {'status': None}


class ApplicationTranslationOptions(TranslationOptions):
    fields = ('title', 'status')
    fallback_undefined = {'status': None}


class CertificationTypeTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'status')
    fallback_undefined = {'status': None}


class DocumentTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class DocumentTranslationOptions(TranslationOptions):
    fields = ('title', 'status', 'file')
    fallback_undefined = {'status': None}


class ExtinguishingAgentTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('characteristics', 'status')
    fallback_undefined = {'status': None}


translator.register(PageTreeItem, PageTreeItemTranslationOptions)
translator.register(WebPage, WebPageTranslationOptions)
translator.register(PageContent, PageContentTranslationOptions)
translator.register(Region, RegionTranslationOptions)
translator.register(NewsCategory, NewsCategoryTranslationOptions)
translator.register(NewsArticle, NewsArticleTranslationOptions)
translator.register(Training, TrainingTranslationOptions)
translator.register(Fair, FairTranslationOptions)
translator.register(TechnologyMapPoint, TechnologyMapPointTranslationOptions)
translator.register(TechnologyFunctionTab, TechnologyFunctionTabTranslationOptions)
translator.register(TechnologyType, TechnologyTypeTranslationOptions)
translator.register(Technology, TechnologyTranslationOptions)
translator.register(SolutionMapPoint, SolutionMapPointTranslationOptions)
translator.register(SolutionType, SolutionTypeTranslationOptions)
translator.register(Solution, SolutionTranslationOptions)
translator.register(ServiceType, ServiceTypeTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(Employee, EmployeeTranslationOptions)
translator.register(Application, ApplicationTranslationOptions)
translator.register(CertificationType, CertificationTypeTranslationOptions)
translator.register(DocumentType, DocumentTypeTranslationOptions)
translator.register(Document, DocumentTranslationOptions)
translator.register(ExtinguishingAgent, ExtinguishingAgentTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
