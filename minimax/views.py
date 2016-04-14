from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect

from .models import WebPage, PageTreeItem, Region, PublishableContent, Technology, Solution, Service
from minimax.utils.translation_utils import get_region


def home(request, region='GL', language_code='en'):
    # TODO: in case region and language are bogus fall back to defaults
    _region, _language_code = get_region(region, language_code)
    return render(request, 'minimax/frontend/home.html',
                  context={'region': _region, 'language_code': _language_code})


def people_akademie(request):
    return render(request, 'minimax/frontend/people-akademie.html')


def page_details(request, region='GL', language_code='en', slug_1=None, slug_2=None, slug=None):
    _region, _language_code = get_region(region, language_code)
    template = 'minimax/frontend/page.html'
    if not slug:
        return redirect('home', region=region, language_code=language_code)
    try:
        if slug_1 == 'solutions' or request.path.startswith('/solutions/'):
            template = 'minimax/frontend/page_solutions.html'
            try:
                solution = Solution.objects.prefetch_related('type', 'projects', 'customers',
                                                             'referenced_technologies').get(slug=slug)
                return render(request, template, context={'page': None, 'solution': solution,
                                                          'region': _region, 'language_code': _language_code,
                                                          'has_customers': solution.customers.count() > 0,
                                                          'has_projects': solution.projects.count() > 0,
                                                          'has_case_studies': False})  # TODO: change after model is added
            except (Solution.DoesNotExist, Solution.MultipleObjectsReturned):
                return redirect('home', region=_region.code, language_code=_language_code)
        if slug_1 == 'technologies' or request.path.startswith('/technologies/'):
            template = 'minimax/frontend/page_technologies.html'
            try:
                technology = Technology.objects.prefetch_related('type', 'referenced_applications', 'projects',
                                                                 'customers', 'function_tabs').get(slug=slug)
                return render(request, template, context={'page': None, 'technology': technology,
                                                          'region': _region, 'language_code': _language_code,
                                                          'has_customers': technology.customers.count() > 0,
                                                          'has_projects': technology.projects.count() > 0,
                                                          'has_function_tabs': technology.function_tabs.count() > 0,
                                                          'has_case_studies': False})  # TODO: change after model is added
            except (Technology.DoesNotExist, Technology.MultipleObjectsReturned):
                return redirect('home', region=_region.code, language_code=_language_code)
        if slug_1 == 'services' or request.path.startswith('/services/'):
            template = 'minimax/frontend/page_services.html'
            try:
                service = Service.objects.prefetch_related('type').get(slug=slug)
                return render(request, template, context={'page': None, 'service': service,
                                                          'region': _region, 'language_code': _language_code,
                                                          'two_columns': True if service.description_right else False
                                                          })
            except (Service.DoesNotExist, Service.MultipleObjectsReturned):
                return redirect('home', region=_region.code, language_code=_language_code)
        if request.user.is_authenticated():
            # allow auth users to see un published pages
            menu_item = PageTreeItem.objects.get(slug=slug)
        else:
            menu_item = PageTreeItem.objects.get(slug=slug, status=PublishableContent.STATUS_PUBLISHED)
        if menu_item.type == PageTreeItem.TYPE_STANDARD:
            # get the page
            try:
                page = WebPage.objects.get(related_page_tree_items__page_tree_item=menu_item,
                                           related_page_tree_items__region=_region)
                if page.template and page.template.path:
                    template = page.template.path
            except WebPage.DoesNotExist:
                # does not exist for the selected region
                global_region = Region.objects.get(code='GL')
                try:
                    page = WebPage.objects.get(related_page_tree_items__page_tree_item=menu_item,
                                               related_page_tree_items__region=global_region)
                except WebPage.DoesNotExist:
                    # does not exist even for global region
                    return redirect('home', region=_region.code, language_code=_language_code)
        else:
            return redirect('home', region=_region.code, language_code=_language_code)

    except PageTreeItem.DoesNotExist:
        # there is no such menu item
        return redirect('home', region=_region.code, language_code=_language_code)

    return render(request, template, context={'page': page, 'region': _region, 'language_code': _language_code})
