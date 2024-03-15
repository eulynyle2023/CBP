from django import template

register = template.Library()

@register.simple_tag
def is_even(counter):
    return counter % 2 == 0