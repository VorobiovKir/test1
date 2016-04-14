from yurl import URL

from django import http
from django.conf import settings
from django.utils.http import is_safe_url
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, override
)

from minimax.models import Region


def get_region(region_code="GL", language_code="en"):
    """
    Get a corresponding Region and language, if active.
    - if the specified language is not active for that region, try the default_language
    - if the default_language is not active for that region fall back to Global - English
    :param region_code: two letter region code, usually from URL
    :param language_code: two letter language code, usually from URL
    :return: Region and the fallback language code
    """
    available_languages = [lang[0] for lang in settings.LANGUAGES]
    try:
        region = Region.objects.get(code=region_code.upper())
        # For bogus language_code set to default_language for that region.
        if language_code not in available_languages:
            language_code = region.default_language
        with override(language_code.lower()):
            if region.active:
                return region, language_code
        # Language not active for the specified language_code, try to fall back to default_language.
        with override(region.default_language):
            if region.active:
                return region, region.default_language
    except Region.DoesNotExist:
        pass
    # Region does not exist or not active for the selected language, or the default language.
    region = Region.objects.get(code='GL')
    return region, 'en'


def set_language_and_region(request, region_code="GL", language_code="en"):
    """
    Adapted from the Django's set_language

    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters, or will be taken from HTTP_REFERER
    """
    next_url = request.POST.get('next', request.GET.get('next'))
    if not is_safe_url(url=next_url, host=request.get_host()):
        next_url = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=next_url, host=request.get_host()):
            next_url = '/GL/en/'  # Default global region with English language.
    # In case of bogus information fall back to default region or language for that region if exists.
    region, new_language_code = get_region(region_code, language_code)
    if new_language_code != language_code:
        language_code = new_language_code

    old_path = URL(next_url).path
    if old_path == "/":
        new_path = "/%s/" % "/".join([region.code, language_code])
    else:
        new_path = "/" + "/".join([region.code, language_code] + old_path.split("/")[3:])
    next_url = URL(next_url).replace(path=new_path)
    response = http.HttpResponseRedirect(next_url)

    if hasattr(request, 'session'):
        request.session[LANGUAGE_SESSION_KEY] = language_code
    else:
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code,
                            max_age=settings.LANGUAGE_COOKIE_AGE,
                            path=settings.LANGUAGE_COOKIE_PATH,
                            domain=settings.LANGUAGE_COOKIE_DOMAIN)
    return response
