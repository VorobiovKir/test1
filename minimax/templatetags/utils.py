import json
from django import template
from django.conf import settings
from django.utils import translation
import os

# The register instance for this particular library
register = template.Library()

# Needs to be before the 'django.contrib.admin' in the INSTALLED_APPS in settings and before simple tags in this file
from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row
@register.inclusion_tag('admin/submit_line.html', takes_context=True)
def submit_row(context):
    ctx = original_submit_row(context)
    ctx.update({
        'show_save_and_add_another': False, # Never show that button
        'show_save_and_continue': context.get('archived_mode_enabled', ctx['show_save_and_continue']), # Hide if archived
        'show_save': context.get('archived_mode_enabled', ctx['show_save']), # Hide if archived
        'show_delete_link': not (context.get('archived_mode_enabled', False) or context.get('archived_mode_disabled', False)) # Hide delete button if archive enabled
    })
    return ctx

@register.simple_tag
def formatted_user_name(user):
    if user.first_name and user.last_name:
        return user.get_full_name()
    else:
        return user.username

@register.simple_tag
def status_css_class(status):
    # The CSS coding convention to be used for transforming status to their related CSS class
    return status.lower().replace('_','-')

@register.simple_tag
def app_version():
    return os.environ.get('APP_VERSION', 'Development')

@register.simple_tag
def panel_css_class_by_fieldset(fieldsets):
    for fieldset in fieldsets: 
        if 'mtg-float-right' in fieldset.classes:
            return 'mtg-left-panel-by-fieldset'
    return ''

@register.simple_tag
def panel_css_class_by_inline(inlines):
    for inline in inlines: 
        if 'mtg-float-right' in inline.opts.classes:
            return 'mtg-left-panel-by-inline'
    return ''

@register.simple_tag
def language_dict_string():
    # Provide the list of languages as JSON dump
    language_dict = dict([(k, translation.ugettext(v)) for k, v in settings.LANGUAGES])
    return json.dumps(language_dict)

@register.simple_tag
def default_language_string():
    # Provide the default language code as string (to be considered the first item in the language dict)
    code, name = settings.LANGUAGES[0]
    return code

@register.simple_tag
def css_branding_file():
    return settings.STATIC_URL + settings.CSS_BRANDING_FILE

@register.filter(name='json')
def tojson(value):
    return json.dumps(value)