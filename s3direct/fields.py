from django.db.models import Field
from django.conf import settings
from s3direct.widgets import S3DirectFileWidget, S3DirectImageWidget


class S3DirectField(Field):
    def __init__(self, *args, **kwargs):
        dest = kwargs.pop('dest', None)
        is_image = kwargs.pop('image', False)
        is_editable = kwargs.pop('editable', False)
        self.widget = S3DirectImageWidget(dest=dest, editable=is_editable) if is_image else S3DirectFileWidget(dest=dest)
        super(S3DirectField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'TextField'

    def formfield(self, *args, **kwargs):
        kwargs['widget'] = self.widget
        return super(S3DirectField, self).formfield(*args, **kwargs)


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^s3direct\.fields\.S3DirectField"])
