from django.utils import timezone
from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
    PrivacyPolicy,
    GoogleAnalytics,
    PopularPost,
    SideBanner1,
    SpHeadBanner1,
)


def common(request):
    category = ParentCategory.objects.all().filter().prefetch_related('subcategory_set')
    subcategory = BlogPost.objects.filter(is_public=True, is_author=False,
                                          created_date__lt=timezone.localtime()).select_related(
        'category').select_related('category__parent').all().order_by('category')
    ranking = PopularPost.objects.select_related('post_id').all().order_by('view_cnt').reverse()
    archive = BlogPost.objects.filter(is_public=True, is_author=False,
                                      created_date__lt=timezone.localtime()).order_by('created_date')
    gatag = GoogleAnalytics.objects.all().values('content')[0]['content'] if GoogleAnalytics.objects.all() else ''
    sidebanner_1 = SideBanner1.objects.all().values('content')[0]['content'] if SideBanner1.objects.all() else ''
    sp_head_banner_1 = SpHeadBanner1.objects.all().values('content')[0]['content'] if SpHeadBanner1.objects.all() else ''
    context = {
        'categories': category,
        'sub_categories': subcategory,
        'ranking': ranking,
        'archive': archive,
        'gatag': gatag,
        'sidebanner_1': sidebanner_1,
        'sp_head_banner_1': sp_head_banner_1,
    }
    return context
