# -*- coding: utf-8 -*-
from django.contrib.admin.widgets import AdminTextareaWidget, ForeignKeyRawIdWidget
from django.contrib.contenttypes.models import ContentType
from django.utils.html import escape

from minimax.utils.text_utils import truncate_words


class AdminRichTextareaWidget(AdminTextareaWidget):
    """
    The default Richtexteditor to be used in the scope of this project.
    """

    def __init__(self, attrs=None):
        final_attrs = {'class': 'vRichTextField'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(AdminRichTextareaWidget, self).__init__(attrs=final_attrs)

    def render(self, name, value, attrs=None):
        return super(AdminRichTextareaWidget, self).render(name=name, value=value, attrs=attrs)

    class Media:
        js = (
            'minimax/tinymce/js/tinymce/tinymce.min.js',
            'minimax/jscripts/richtext_editor.js',
        )
        css = {
            'all': ['minimax/css/richtext_editor.css']
        }


class ForeignKeyRawIdWidgetWithLink(ForeignKeyRawIdWidget):
    """
    A enriched version of Grappellie's default widget that show the related entity as link.
    """

    def label_for_value(self, value):
        key = self.rel.get_related_field().name
        try:
            content_type_id = ContentType.objects.get_for_model(self.rel.to).pk
            obj = self.rel.to._default_manager.using(self.db).get(**{key: value})
            obj_link = '../../../r/%s/%s/' % (content_type_id, obj.pk)
            obj_preview = escape(truncate_words(obj, 14))
            return (
                '&nbsp;<strong>'
                '<a href="%s" class="raw-id-viewsite-link" title="View on Site" target="_blank">%s</a>'
                '</strong>' % (obj_link, obj_preview)
            )
        except (ValueError, self.rel.to.DoesNotExist):
            return ''
