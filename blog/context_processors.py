from django.utils import timezone
from django.conf import settings
from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
    PrivacyPolicy,
    GoogleAnalytics,
    PopularPost,
)
import json

# ランキング用の記事番号取得
f = open(settings.BASE_DIR+'/blog/data/rank.json', 'r')
rank_list = [k for k in json.load(f).keys()]
f.close()


def common(request):
    category = ParentCategory.objects.all().filter().prefetch_related('subcategory_set')
    subcategory = BlogPost.objects.filter(is_public=True, is_author=False,
                                          created_date__lt=timezone.localtime()).select_related(
        'category').select_related('category__parent').all().order_by('category')
    ranking = PopularPost.objects.select_related('post_id').all().order_by('view_cnt')
    print(ranking)
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
