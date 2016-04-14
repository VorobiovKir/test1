# -*- coding: utf-8 -*-
from django.utils.functional import allow_lazy
from django.utils.text import Truncator


def truncate_words(s, num, end_text='...'):
    """
    Truncates the given string based on the given parameters.

    :param s: The string to truncate
    :param num: Number of words after which to truncate
    :param end_text: The string to be used as place holder to further text
    :return: The truncated string
    """
    truncate = end_text and ' %s' % end_text or ''
    return Truncator(s).words(num, truncate=truncate)


truncate_words = allow_lazy(truncate_words, unicode)


def truncate_chars(s, num, end_text='...'):
    """
    Truncates the given string based on the given parameters.

    :param s: The string to truncate
    :param num: Number of characters after which to truncate
    :param end_text: The string to be used as place holder to further text
    :return: The truncated string
    """
    truncate = end_text and ' %s' % end_text or ''
    return Truncator(s).chars(num, truncate=truncate)


truncate_words = allow_lazy(truncate_words, unicode)
