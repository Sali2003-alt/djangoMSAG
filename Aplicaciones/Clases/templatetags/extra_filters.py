# Aplicaciones/Clases/templatetags/extra_filters.py
from django import template

register = template.Library()

@register.filter
def is_mp4(value):
    return value.endswith('.mp4')

@register.filter
def is_pdf(value):
    return value.endswith('.pdf')
