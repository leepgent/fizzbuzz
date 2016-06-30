# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import template
import string
import io
register = template.Library()


@register.filter
def censor(value):
    s = io.StringIO()
    for c in value:
        if c in string.letters:
            s.write('x')
        else:
            s.write(c)

    return s.getvalue()
