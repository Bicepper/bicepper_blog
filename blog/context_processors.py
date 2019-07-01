from django.db.models import Prefetch
from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
    PrivacyPolicy,
    GoogleAnalytics,
)


def common(request):
    category = ParentCategory.objects.all().prefetch_related('subcategory_set')
    subcategory = BlogPost.objects.select_related('category').select_related('category__parent').all().order_by('category')
    ranking = BlogPost.objects.all().order_by('hit_count_generic')[:3]
    archive = BlogPost.objects.order_by('created_date')
    gatag = GoogleAnalytics.objects.all().values('content')[0]['content'] if GoogleAnalytics.objects.all() else ''
    context = {
        'categories': category,
        'sub_categories': subcategory,
        'ranking': ranking,
        'archive': archive,
        'gatag': gatag,
    }
    return context
