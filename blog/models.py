import os
import pytz
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from uuid import uuid4
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from filebrowser.fields import FileBrowseField
from froala_editor.fields import FroalaField
from hitcount.models import HitCount
from hitcount.models import HitCountMixin


class ParentCategory(models.Model):
    title = models.CharField(_('カテゴリ名'), max_length=255, unique=True)
    slug = models.SlugField(_('スラッグ'), default='', null=False, blank=False, unique=True)

    class Meta:
        verbose_name = _('カテゴリ')
        verbose_name_plural = _('カテゴリ')

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(_('カテゴリ名'), max_length=255, unique=True)
    parent = models.ForeignKey('ParentCategory', on_delete=models.CASCADE)
    slug = models.SlugField(_('スラッグ'), default='', null=False, blank=False, unique=True)

    class Meta:
        verbose_name = _('サブカテゴリ')
        verbose_name_plural = _('サブカテゴリ')

    def __str__(self):
        return self.title


class BlogPost(models.Model, HitCountMixin):
    author = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE, verbose_name=_('作成者'))
    main_image = FileBrowseField("メイン画像", max_length=200, directory="media/uploads/thumbnail/",
                                 extensions=[".jpg", ".png"], blank=False, null=True)
    category = models.ForeignKey('SubCategory', verbose_name='カテゴリ', default=3, on_delete=models.PROTECT)
    title = models.CharField(_('タイトル'), max_length=33, blank=False)
    description = models.TextField(_('記事概要'), max_length=108, default='', blank=False)
    content = FroalaField(_('内容'), default='', blank=False, null=False)
    created_date = models.DateTimeField(_('作成日'), default=timezone.now, blank=False)
    published_date = models.DateTimeField(_('更新日'), blank=True, null=True)
    is_public = models.BooleanField(_('公開設定'), default=True, help_text='非公開にする場合はチェックを入れる')
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')
    relation_posts = models.ManyToManyField('self', verbose_name='関連記事', blank=True)

    class Meta:
        verbose_name = _('投稿')
        verbose_name_plural = _('投稿')
        ordering = ['-created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def path_and_rename(self, filename):
        prefix = "main_image"
        name = str(uuid4()).replace('-', '')
        extension = os.path.splitext(filename)[-1]
        return prefix + name + extension

    def summary(self):
        return self.content[:30] + '...'

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(_('名前（表示名）'), blank=False, max_length=255)
    author_image = FileBrowseField("メイン画像", max_length=200, directory="media/uploads/profile/",
                                   extensions=[".jpg", ".png"], blank=False, null=True)
    content = FroalaField(_('内容'), default='', blank=False, null=False)
    created_date = models.DateTimeField(_('作成日'), default=timezone.now, blank=False)
    published_date = models.DateTimeField(_('更新日'), blank=True, null=True)
    is_public = models.BooleanField(_('公開設定'), default=True, help_text='非公開にする場合はチェックを入れる')

    class Meta:
        verbose_name = _('プロフィール')
        verbose_name_plural = _('プロフィール')

    def __str__(self):
        return self.name


class PrivacyPolicy(models.Model):
    content = FroalaField(_('内容'), default='', blank=False, null=False)
    created_date = models.DateTimeField(_('作成日'), default=timezone.now, blank=False)
    published_date = models.DateTimeField(_('更新日'), blank=True, null=True)
    is_public = models.BooleanField(_('公開設定'), default=True, help_text='非公開にする場合はチェックを入れる')

    class Meta:
        verbose_name = _('Privacy&Policy')
        verbose_name_plural = _('Privacy&Policy')

    def __str__(self):
        return 'Privacy&Policy'


