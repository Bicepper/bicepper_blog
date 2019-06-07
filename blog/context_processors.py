from .models import (
    ParentCategory,
    SubCategory,
    BlogPost,
)


def common(request):
    category = SubCategory.objects.all().values('parent__slug', 'slug')
    print("ejwaofwjaifwae:{}".format(category))
    context = {
        'categories': category,
    }
    return context
