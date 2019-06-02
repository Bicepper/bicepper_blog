from django import template
import re
register = template.Library()


@register.filter(name="time_split", is_safe=True, needs_autoescape=True)
def time_split(value, autoescape=True):
    test = str(value)
    display_time = test.split(" ")
    print(display_time)
    return test
