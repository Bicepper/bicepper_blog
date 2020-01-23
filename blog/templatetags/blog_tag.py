from django import template
from django.utils import timezone
import re
register = template.Library()


@register.filter(name="time_split", is_safe=True, needs_autoescape=True)
def time_split(value, autoescape=True):
    res = value.split("/")
    display_time = "{}年{}月".format(res[1], res[2])
    return display_time
