from django.db.models import Prefetch
from django.utils import timezone
from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
    PrivacyPolicy,
    GoogleAnalytics,
)


def common(request):
    category = ParentCategory.objects.all().filter().prefetch_related('subcategory_set')
    subcategory = BlogPost.objects.filter(is_public=True, is_author=False,
                                          created_date__lt=timezone.localtime()).select_related(
        'category').select_related('category__parent').all().order_by('category')
    ranking = BlogPost.objects.all().filter(is_public=True, is_author=False,
                                            created_date__lt=timezone.localtime()).order_by('hit_count_generic')[:3]
    archive = BlogPost.objects.filter(is_public=True, is_author=False,
                                      created_date__lt=timezone.localtime()).order_by('created_date')
    gatag = GoogleAnalytics.objects.all().values('content')[0]['content'] if GoogleAnalytics.objects.all() else ''
    context = {
        'categories': category,
        'sub_categories': subcategory,
        'ranking': ranking,
        'archive': archive,
        'gatag': gatag,
    }
    return context
