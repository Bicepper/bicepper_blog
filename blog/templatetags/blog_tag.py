from django import template
from django.utils import timezone
import re
register = template.Library()


@register.filter(name="time_split", is_safe=True, needs_autoescape=True)
def time_split(value, autoescape=True):
    res = str(timezone.localtime(value))
    display_time = res.split(" ")[0]
    return display_time
