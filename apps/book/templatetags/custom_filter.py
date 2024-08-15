from django import template

register = template.Library()

@register.filter
def semi_colon_separator(value):
    return value.replace(', ', '; ')
