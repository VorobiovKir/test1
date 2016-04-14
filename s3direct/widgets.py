import os

from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.conf import settings


class S3DirectFileWidget(widgets.TextInput):

    default_html = (
        '<div class="s3direct" data-policy-url="{policy_url}">'
        '  <a class="file-link" target="_blank" href="{file_url}">{file_name}</a>'
        '  <a class="file-remove" href="#remove"></a>'
        '  <input class="file-url{input_class}" type="hidden" value="{file_url}" id="{element_id}" name="{name}" />'
        '  <input class="file-dest" type="hidden" value="{dest}">'
        '  <input class="file-input" type="file" />'
        '  <div class="progress progress-striped active">'
        '    <div class="bar"></div>'
        '  </div>'
        '</div>'
    )

    class Media:
        js = (
            's3direct/js/scripts.js',
        )
        css = {
            'all': (
                's3direct/css/bootstrap-progress.min.css',
                's3direct/css/styles.css',
            )
        }

    def __init__(self, *args, **kwargs):
        self.image = kwargs.pop('image', False)
        self.editable = kwargs.pop('editable', False)
        self.dest = kwargs.pop('dest', None)
        self.html = kwargs.pop('html', self.default_html)
        super(S3DirectFileWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, name=name)
        output = self.html.format(
            policy_url=reverse('s3direct'),
            element_id=final_attrs.get('id'),
            file_name=os.path.basename(value or ''),
            dest=self.dest,
            image=self.image,
            editable=self.editable,
            file_url=value or '',
            input_class=final_attrs.get('class'),
            name=name)

        return mark_safe(output)


class S3DirectImageWidget(S3DirectFileWidget):
    edit_button = '<a class="file-edit" href="#edit" data-target="#edit-%s"></a>'

    default_html = (
        '<div class="s3direct" data-policy-url="{policy_url}">'
        '  <a class="file-thumb" target="_blank" href="{file_url}">'
        '    <img alt="{file_name}" src="{file_url}" alt="{file_name}" />'
        '  </a>'
        '  <a class="file-remove" href="#remove"></a>'
        '  {edit_button}'
        '  <input class="file-url{input_class}" type="hidden" value="{file_url}" id="{element_id}" name="{name}" />'
        '  <input class="file-dest" type="hidden" value="{dest}">'
        '  <input class="file-input" type="file" />'
        '  <div class="progress progress-striped active">'
        '    <div class="bar"></div>'
        '  </div>'
        '  <div class="file-edit-modal-wrapper" id="edit-{element_id}">'
        '    <div class="file-edit-modal">'
        '      <div class="file-edit-image">'
        '        <img src="" />'
        '      </div>'
        '      <button class="file-cancel grp-button grp-delete-link">Cancel</button>'
        '      <button class="file-save grp-button">Save</button>'
        '    </div>'
        '  </div>'
        '</div>'
    )

    class Media:
        js = (
            's3direct/js/cropper.js',
            's3direct/js/scripts.js',
        )
        css = {
            'all': (
                's3direct/css/bootstrap-progress.min.css',
                's3direct/css/cropper.css',
                's3direct/css/styles.css',
            )
        }

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, name=name)
        output = self.html.format(
            policy_url=reverse('s3direct'),
            element_id=final_attrs.get('id'),
            file_name=os.path.basename(value or ''),
            dest=self.dest,
            image=self.image,
            editable=self.editable,
            file_url=value or '',
            input_class=final_attrs.get('class'),
            edit_button=self._get_edit_button(final_attrs),
            name=name)

        return mark_safe(output)

    def _get_edit_button(self, attrs):
        return self.edit_button % attrs.get('id', '') if self.editable else ''
