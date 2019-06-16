import datetime
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import MonthArchiveView
from django.db.models.functions import Trunc, TruncYear, TruncMonth
from django.contrib.sites.shortcuts import get_current_site
from django.urls import resolve
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
        queryset = BlogPost.objects.filter(is_public=True, created_date__lt=datetime.datetime.now()).order_by('-created_date').select_related('category')
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


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'

    def get_object(self, queryset=None):
        post = super().get_object()
        if post.is_public:
            return post
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_site = get_current_site(self.request)
        current_domain = current_site.domain
        url = '{0}://{1}/{2}/{3}'.format(self.request.scheme, current_domain, resolve(self.request.path_info).url_name,
                                         resolve(self.request.path_info).kwargs['pk'])

        context['social_url'] = url
        return context






