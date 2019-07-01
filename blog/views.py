import json
import datetime
from urllib import parse
from urllib import request
from django.contrib import messages
from django.utils import timezone
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import MonthArchiveView
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.contrib.sites.shortcuts import get_current_site
from django.urls import resolve
from django.db.models import Q
from django.conf import settings
from .models import BlogPost
from .models import ParentCategory
from .models import SubCategory
from .forms import BlogPostSearch
from .forms import ContactForm
from .models import Profile
from .models import PrivacyPolicy


class BaseListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    paginate_by = 8
    form_class = BlogPostSearch
    search_text = None

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        self.search_text = search_query
        queryset = BlogPost.objects.filter(is_public=True, is_author=False, created_date__lt=timezone.localtime()) \
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
        return context


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
        return year

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_public=True, is_author=False, created_date__lt=timezone.localtime()) \
            .order_by('-created_date')
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
        elif post.is_public is False and self.request.user.is_authenticated:
            return post
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # social用のURL生成
        current_site = get_current_site(self.request)
        current_domain = current_site.domain
        url = '{0}://{1}/{2}/{3}'.format(self.request.scheme, current_domain, resolve(self.request.path_info).url_name,
                                         resolve(self.request.path_info).kwargs['pk'])

        # 現在日時と投稿日の差を取得
        now_time = datetime.datetime.now().replace(microsecond=0)
        post_time = BlogPost.objects.filter(pk=self.kwargs['pk']).values('created_date')[0]['created_date'].replace(tzinfo=None)

        context['social_url'] = url
        context['test_form'] = self.form_class()
        context['time_elapsed'] = int(str(now_time - post_time).split()[0]) if len(str(now_time - post_time).split(",")) >= 2 else 0  # 差分0日だとエラーになるので

        return context


class ProfileView(TemplateView):
    model = Profile
    template_name = 'profile.html'
    form_class = BlogPostSearch

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile'] = Profile.objects.all()
        context['test_form'] = self.form_class()
        return context


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'test_form': BlogPostSearch
        })
        context['recaptcha_site_id'] = settings.GOOGLE_RECAPTCHA_SITE_KEY
        return context

    def form_valid(self, form):
        form.send_email(self.request)

        # recaptcha取得
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = parse.urlencode(payload).encode()
        req = request.Request(url, data=data)

        # 送信されたトークンが有効であることを確認
        response = request.urlopen(req)
        result = json.loads(response.read().decode())

        if not result['success']:  # make sure action matches the one from your template
            messages.error(self.request, 'reCAPTCHAの承認に失敗しました。時間を置いて再度お試しください。')
            return super().form_invalid(form)
        else:
            return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'contact/contact_result.html'
    form_class = BlogPostSearch

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = 'お問い合わせいただきありがとうございます。<br>正常に送信されました。<br>なお、全ての問い合わせに返信はしておりませんことをご了承ください。'
        context['test_form'] = BlogPostSearch
        return context


class PrivacyPolicyView(TemplateView):
    model = PrivacyPolicy
    template_name = 'privacy.html'
    form_class = BlogPostSearch

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile'] = PrivacyPolicy.objects.all()
        context['test_form'] = self.form_class()
        return context


def ip_check(request, *args, **kwargs):
    ip = request.META['REMOTE_ADDR']
    return ip

