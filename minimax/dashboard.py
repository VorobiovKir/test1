# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.modules import DashboardModule
from grappelli.dashboard.utils import get_admin_site_name


class RecentActions(DashboardModule):
    """
    Module that lists the recent actions.
    """

    title = _('Recent Actions')
    template = 'minimax/dashboard/recent_actions.html'
    limit = 10
    include_list = None
    exclude_list = None

    def __init__(self, title=None, limit=10, include_list=None,
                 exclude_list=None, limit_to_requesting_user=False, **kwargs):
        self.include_list = include_list or []
        self.exclude_list = exclude_list or []
        self.limit_to_requesting_user = limit_to_requesting_user
        kwargs.update({'limit': limit})
        super(RecentActions, self).__init__(title, **kwargs)

    def init_with_context(self, context):
        if self._initialized:
            return
        from django.db.models import Q
        from django.contrib.admin.models import LogEntry

        request = context['request']

        def get_qset(list):
            qset = None
            for contenttype in list:
                if isinstance(contenttype, ContentType):
                    current_qset = Q(content_type__id=contenttype.id)
                else:
                    try:
                        app_label, model = contenttype.split('.')
                    except:
                        raise ValueError('Invalid contenttype: "%s"' % contenttype)
                    current_qset = Q(
                        content_type__app_label=app_label,
                        content_type__model=model
                    )
                if qset is None:
                    qset = current_qset
                else:
                    qset = qset | current_qset
            return qset

        if self.limit_to_requesting_user:
            qs = LogEntry.objects.filter(user__id__exact=request.user.id)
        else:
            qs = LogEntry.objects.all()

        if self.include_list:
            qs = qs.filter(get_qset(self.include_list))
        if self.exclude_list:
            qs = qs.exclude(get_qset(self.exclude_list))

        self.children = qs.select_related('content_type', 'user')[:self.limit]
        self._initialized = True


class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.Group(
            _(u'Web site navigation'),
            column=1,
            collapsible=True,
            children=[
                modules.ModelList(
                    models=('minimax.models.PageTreeItem',),
                ),
            ]
        ))

        self.children.append(modules.Group(
            _(u'Web content management'),
            column=1,
            collapsible=True,
            children=[
                modules.ModelList(
                    models=('minimax.models.WebPage',),
                ),
                modules.ModelList(
                    title=_(u'News & event management'),
                    models=('minimax.models.NewsArticle', 'minimax.models.Training', 'minimax.models.Fair'),
                ),
                modules.ModelList(
                    title=_(u'People feature'),
                    models=('minimax.models.Employee',),
                )
            ]
        ))

        self.children.append(modules.Group(
            _(u'Technologies'),
            column=1,
            collapsible=True,
            children=[
                modules.ModelList(
                    models=('minimax.models.TechnologyType', 'minimax.models.Technology'),
                )
            ]
        ))

        self.children.append(modules.Group(
            _(u'Solutions'),
            column=1,
            collapsible=True,
            children=[
                modules.ModelList(
                    models=('minimax.models.SolutionType', 'minimax.models.Solution'),
                )
            ]
        )),

        self.children.append(modules.Group(
            _(u'Services'),
            column=1,
            collapsible=True,
            children=[
                modules.ModelList(
                    models=('minimax.models.ServiceType', 'minimax.models.Service'),
                )
            ]
        )),

        self.children.append(modules.Group(
            _(u'Others'),
            column=1,
            collapsible=True,
            children=[
                modules.ModelList(
                    models=('minimax.models.Application',),
                )
            ]
        )),

        self.children.append(modules.ModelList(
            title=_(u'Global settings'),
            column=2,
            collapsible=False,
            models=('minimax.models.Region', 'minimax.models.Template', 'minimax.models.CertificationType',
                    'minimax.models.ExtinguishingAgent'),
        )),

        self.children.append(modules.ModelList(
            title=_(u'Download center'),
            column=2,
            collapsible=False,
            models=('minimax.models.DocumentType', 'minimax.models.Document'),
        )),

        self.children.append(modules.Group(
            _(u'References'),
            column=2,
            collapsible=False,
            models=('minimax.models.Customer', 'minimax.models.Project')
        )),

        self.children.append(modules.ModelList(
            title=_(u'Security'),
            column=2,
            collapsible=False,
            models=('django.contrib.auth.models.User', 'django.contrib.auth.models.Group'),
        )),

        # Append "my last actions"
        self.children.append(modules.RecentActions(
            _(u'My last activities'),
            limit=3,
            collapsible=False,
            column=2,
        )),

        # Append a recent actions module
        self.children.append(RecentActions(
            _(u'Activity stream'),
            limit=20,
            collapsible=False,
            column=3,
        ))
