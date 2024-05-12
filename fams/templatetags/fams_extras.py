from django import template

register = template.Library()

@register.filter(name="shift")
def shift(value):
    if value == '1':
        return "Morning"
    elif value == '2':
        return "Evening"
    else:
        return value.title()
