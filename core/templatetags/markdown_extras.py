from django import template
from django.template.defaultfilters import stringfilter

import markdown as md
register = template.Library()

@register.filter()
@stringfilter
def markdown(values):
    return md.markdown( values, extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'] )