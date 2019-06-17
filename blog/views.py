from django.utils import timezone
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import MonthArchiveView
from django.views.generic import TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.urls import resolve
from django.core.paginator import Paginator
from django.db.models import Q
from .models import BlogPost
from .models import ParentCategory
from .models import SubCategory
from .forms import BlogPostSearch
from .models import Profile
from django.views.generic.edit import ModelFormMixin


class BaseListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    paginate_by = 8
    form_class = BlogPostSearch
    search_text = None

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        self.search_text = search_query
        queryset = BlogPost.objects.filter(is_public=True, created_date__lt=timezone.localtime()) \
            .order_by('-created_date').select_related('category')

        if search_query is not None:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query) |
                Q(description__contains=search_query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_form'] = self.form_class()
        context['search_text'] = self.search_text
        print('確認:{}'.format(self.search_text))
        return context


class PostList(BaseListView):

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    # def get(self, request, *args, **kwargs):
    #     search_query = self.request.GET.get('title')
    #     print('検索ワード:{}'.format(search_query))


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
    paginate_by = 8
    date_field = 'created_date'
    month_format = '%m'
    year_format = '%Y'
    allow_future = True
    form_class = BlogPostSearch

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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['test_form'] = self.form_class()

        return context


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    form_class = BlogPostSearch

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
        context['test_form'] = self.form_class()
        return context


class ProfileView(TemplateView):
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile'] = Profile.objects.all()
        return context




