from django.db.models import Prefetch
from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
)


def common(request):
    category = ParentCategory.objects.all().prefetch_related('subcategory_set')
    subcategory = BlogPost.objects.select_related('category').select_related('category__parent').all().order_by('category')
    ranking = BlogPost.objects.all().order_by('hit_count_generic')[:3]
    archive = BlogPost.objects.order_by('created_date')
    context = {
        'categories': category,
        'sub_categories': subcategory,
        'ranking': ranking,
        'archive': archive,
    }
    return context
