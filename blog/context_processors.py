from django.contrib.sites.shortcuts import get_current_site
from .models import (
    Category,
    BlogPost,
)


def common(request):
    site = get_current_site(request)
    category = Category.objects.all()
    print(category['slug'])
    context = {
        'categories': category,
    }
    return context
