from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    author = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(default='', blank=False, null=False)
    created_date = models.TimeField(default=timezone.now, blank=False)
    published_date = models.DateTimeField(blank=True, null=True)
    live = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
