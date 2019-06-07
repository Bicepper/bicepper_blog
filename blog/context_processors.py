from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
)


def common(request):
    category = ParentCategory.objects.all()
    subcategory = SubCategory.objects.all().values('parent__slug', 'slug')
    print("ejwaofwjaifwae:{}".format(category))
    print("dddddddddddddd:{}".format(subcategory))
    context = {
        'categories': category,
        'sub_categories': subcategory,
    }
    return context
