from django.contrib.sites.shortcuts import get_current_site
from .models import (
    Category,
    BlogPost,
)


def common(request):
    site = get_current_site(request)
    context = {
        'categories': Category.objects.all(),
    }
    return context
