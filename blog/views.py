from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import MonthArchiveView
from django.db.models.functions import Trunc, TruncYear, TruncMonth
from .models import BlogPost
from .models import ParentCategory
from .models import SubCategory

import pytz
import datetime


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
        category = ParentCategory.objects.get(slug=category_name).slug
        queryset = super().get_queryset().filter(category__parent__slug=category)
        return queryset


class SubCategoryList(BaseListView):
    def get_queryset(self):
        category_name = self.kwargs['category__slug']
        category = SubCategory.objects.get(slug=category_name)
        queryset = super().get_queryset().filter(category=category)
        return queryset


class ArchiveList(MonthArchiveView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    date_field = 'created_date'
    month_format = '%m'
    year_format = '%Y'
    allow_future = True

    def get_month(self):
        month = super(ArchiveList, self).get_month()
        return month

    def get_year(self):
        year = super(ArchiveList, self).get_year()
        print('年:{}'.format(year))
        return year

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

# class ArchiveList(BaseListView):
#     def get_queryset(self):
#         queryset = BlogPost.objects.filter(created_date__year='2019', created_date__month='5')
#         print(queryset)
#         return queryset


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'

    def get_object(self, queryset=None):
        post = super().get_object()
        if post.is_public:
            return post
        else:
            raise Http404

