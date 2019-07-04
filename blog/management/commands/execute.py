from django.core.management.base import BaseCommand
from .HelloAnalytics import get_10_popular
from blog.models import PopularPost


class Command(BaseCommand):

    def handle(self, *args, **options):
        PopularPost.objects.all().delete()
        for post_pk, page_view in get_10_popular():
            PopularPost.objects.create(post_id_id=post_pk.split("/")[2], view_cnt=page_view)

