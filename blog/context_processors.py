from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
)


def common(request):
    category = SubCategory.objects.all().values_list('slug', flat=True)
    context = {
        'categories': category,
    }
    return context
