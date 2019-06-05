from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import View
from .models import BlogPost
from .models import Category


class BaseListView(ListView):
    paginate_by = 10
    model = BlogPost
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_public=True).order_by('-created_date').select_related('category')
        return queryset


class PostList(BaseListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class CategoryList(BaseListView):
    def get_queryset(self):
        category_name = self.kwargs['category']
        category = Category.objects.get(name=category_name)
        queryset = super().get_queryset().filter(category=category)
        return queryset
