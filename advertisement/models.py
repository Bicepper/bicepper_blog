from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from blog.models import (
    ParentCategory,
    SubCategory
)


class AdvertisementBlogFooter(models.Model):
    category = models.ForeignKey(SubCategory, verbose_name="表示カテゴリー", default=3, on_delete=models.PROTECT)
    title = models.TextField(_("広告タイトル"), max_length=255, blank=True)
    content = RichTextField(_("内容"), default='', blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("ブログフッター広告")
        verbose_name_plural = _("ブログフッター広告")


class AdvertisementBlogSide(models.Model):
    category = models.ForeignKey(SubCategory, verbose_name="表示カテゴリー", default=3, on_delete=models.PROTECT)
    title = models.TextField(_("広告タイトル"), max_length=255, blank=True)
    content = RichTextField(_("内容"), default='', blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("ブログサイド広告")
        verbose_name_plural = _("ブログサイド広告")



