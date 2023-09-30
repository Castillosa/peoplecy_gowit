from django import template

register = template.Library()


@register.filter()
def range_(min=5):
    return range(min)
