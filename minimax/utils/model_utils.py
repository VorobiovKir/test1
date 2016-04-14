# -*- coding: utf-8 -*-
from django.db import models


class RichTextField(models.TextField):
    """
    Proxy class to be used on UI level to render the default RTE widget.
    """
    pass

