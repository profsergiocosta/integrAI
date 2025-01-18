from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    print (value, arg)
    return value * arg if value is not None and arg is not None else 0


@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
