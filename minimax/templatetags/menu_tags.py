from django import template
from django.conf import settings
from django.utils import translation
from django.template import Context

from minimax.models import PageTreeItem, TechnologyType, PublishableContent, SolutionType, ServiceType, Region

# The register instance for this particular library
register = template.Library()


def get_menu_items():
    """
    Gets the list of menu items to be used in menu rendering.
    The result should be cached to decrease the database queries.
    :return: a list of menu items to be rendered in menus
    """
    _menu_items = PageTreeItem.objects.all().filter(parent__type=PageTreeItem.TYPE_HOME,
                                                    status=PageTreeItem.STATUS_PUBLISHED)
    menu_items = []
    for menu_item in _menu_items:
        menu_class = ''
        if menu_item.type == PageTreeItem.TYPE_TECHNOLOGIES:
            _technology_types = []
            technology_types = TechnologyType.objects.prefetch_related('technologies')\
                .filter(technologies__status=PublishableContent.STATUS_PUBLISHED).order_by('name').distinct()
            for _type in technology_types:
                _technologies = []
                for tech in _type.technologies.filter(status=PublishableContent.STATUS_PUBLISHED):
                    _technologies.append({'name': tech.name, 'url': tech.get_absolute_url,
                                          'type': PageTreeItem.TYPE_STANDARD})  # standard types have links
                _technology_types.append({'name': _type.name, 'children': _technologies})
            menu_items.append({
                'name': menu_item.name,
                'children': _technology_types,
                'menu_class': 'technologies',
                'has_grandchildren': True,
                'title': menu_item.title,
                'teaser': menu_item.teaser,
                'slug': menu_item.slug,
            })
        elif menu_item.type == PageTreeItem.TYPE_SOLUTIONS:
            _solution_types = []
            solution_types = SolutionType.objects.prefetch_related('solutions')\
                .filter(solutions__status=PublishableContent.STATUS_PUBLISHED).order_by('name').distinct()
            for _type in solution_types:
                _solutions = []
                for solution in _type.solutions.filter(status=PublishableContent.STATUS_PUBLISHED):
                    _solutions.append({'name': solution.name, 'url': solution.get_absolute_url,
                                       'type': PageTreeItem.TYPE_STANDARD})
                _solution_types.append({'name': _type.name, 'children': _solutions})
            menu_items.append({
                'name': menu_item.name,
                'children': _solution_types,
                'menu_class': 'solutions',
                'has_grandchildren': True,
                'title': menu_item.title,
                'teaser': menu_item.teaser,
                'slug': menu_item.slug,
            })
        elif menu_item.type == PageTreeItem.TYPE_SERVICES:
            _service_types = []
            service_types = ServiceType.objects.prefetch_related('services')\
                .filter(services__status=PublishableContent.STATUS_PUBLISHED).order_by('name').distinct()
            for _type in service_types:
                _services = []
                for service in _type.services.filter(status=PublishableContent.STATUS_PUBLISHED):
                    _services.append({'name': service.name, 'url': service.get_absolute_url,
                                      'type': PageTreeItem.TYPE_STANDARD})
                _service_types.append({'name': _type.name, 'children': _services})
            menu_items.append({
                'name': menu_item.name,
                'children': _service_types,
                'menu_class': 'service',
                'has_grandchildren': True,
                'title': menu_item.title,
                'teaser': menu_item.teaser,
                'slug': menu_item.slug,

            })
        else:
            if menu_item.slug == 'people':
                menu_class = 'people'
            has_grandchildren = False
            _children = []
            for child in menu_item.children.filter(status=PublishableContent.STATUS_PUBLISHED):
                _grands = []
                for grand in child.children.filter(status=PublishableContent.STATUS_PUBLISHED):
                    has_grandchildren = True
                    _grands.append({'name': grand.name, 'url': grand.get_absolute_url,
                                    'type': PageTreeItem.TYPE_STANDARD})
                _children.append({'name': child.name, 'children': _grands, 'type': child.type,
                                  'url': child.get_absolute_url})
            menu_items.append({
                'name': menu_item.name,
                'type': menu_item.type,
                'children': _children,
                'has_grandchildren': has_grandchildren,
                'menu_class': menu_class,
                'title': menu_item.title,
                'teaser': menu_item.teaser,
                'slug': menu_item.slug,
                'url': menu_item.get_absolute_url,
            })
    return menu_items


@register.inclusion_tag('minimax/frontend/includes/top_menu.html', takes_context=True)
def render_top_menu(context):
    """
    Renders the general top menu, for large screen devices.
    """
    new_context = Context(context, autoescape=context.autoescape)
    new_context['menu_items'] = get_menu_items()
    return new_context


@register.inclusion_tag('minimax/frontend/includes/top_menu_mobile.html', takes_context=True)
def render_top_menu_mobile(context):
    """
    Renders the menu for the mobile devices.
    """
    new_context = Context(context, autoescape=context.autoescape)
    new_context['menu_items'] = get_menu_items()
    return new_context


@register.assignment_tag(takes_context=False)
def get_active_regions():
    """
    Returns a list with Regions and their active languages.
    :return: List with active regions
    """
    regions = []
    for region in Region.objects.all():
        for language in settings.LANGUAGES:
            with translation.override(language[0]):
                if region.active:
                    regions.append({'name': region, 'region_code': region.code,
                                    'language_code': language[0], 'language_name': language[1]})
    return regions
