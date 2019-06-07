from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import View
from .models import BlogPost
from .models import ParentCategory
from .models import SubCategory


class BaseListView(ListView):
    paginate_by = 10
    model = BlogPost
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_public=True).order_by('-created_date').select_related('category')
        print(queryset.values('category__parent__slug', 'category__slug'))
        return queryset


class PostList(BaseListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print('これcontext：{}'.format(context['object_list']))
    #     return context


class CategoryList(BaseListView):
    def get_queryset(self):
        category_name = self.kwargs['category']
        category = SubCategory.objects.get(name=category_name)
        queryset = super().get_queryset().filter(category=category)
        return queryset


class SubCategoryList(BaseListView):
    def get_queryset(self):
        category_name = self.kwargs['category__slug']
        print('kwargsのデータ{}'.format(category_name))
        category = SubCategory.objects.get(slug=category_name)
        queryset = super().get_queryset().filter(category=category)
        return queryset

