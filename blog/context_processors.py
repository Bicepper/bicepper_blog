from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
)


def common(request):
    category = ParentCategory.objects.all()
    subcategory = SubCategory.objects.all().values('parent__slug', 'slug')
    ranking = BlogPost.objects.all().order_by('hit_count_generic')[:3]
    archive = BlogPost.objects.order_by('created_date')
    context = {
        'categories': category,
        'sub_categories': subcategory,
        'ranking': ranking,
        'archive': archive,
    }
    return context
