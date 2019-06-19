from django.db.models import Prefetch
from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
)


def common(request):
    category = ParentCategory.objects.all().prefetch_related('subcategory_set')
    for ct in category:
        print(ct.subcategory_set.all())
    subcategory = SubCategory.objects.all().values('parent__title', 'parent__slug', 'slug')
    ranking = BlogPost.objects.all().order_by('hit_count_generic')[:3]
    archive = BlogPost.objects.order_by('created_date')
    context = {
        'categories': category,
        'sub_categories': subcategory,
        'ranking': ranking,
        'archive': archive,
    }
    return context
