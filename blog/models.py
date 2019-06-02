import os
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from uuid import uuid4
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from filebrowser.fields import FileBrowseField
from froala_editor.fields import FroalaField


class BlogPost(models.Model):
    author = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE, verbose_name=_('作成者'))
    main_image = FileBrowseField("メイン画像", max_length=200, directory="media/uploads/thumbnail/", extensions=[".jpg"],
                                 blank=False, null=True)
    title = models.CharField(_('タイトル'), max_length=200, blank=False)
    content = FroalaField(_('内容'), default='', blank=False, null=False)
    created_date = models.DateTimeField(_('作成日'), default=timezone.now, blank=False)
    published_date = models.DateTimeField(_('更新日'), blank=True, null=True)

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

    def __str__(self):
        return self.title
