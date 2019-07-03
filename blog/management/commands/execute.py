from django.conf import settings
from django.core.management.base import BaseCommand
from .HelloAnalytics import get_10_popular

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        # 過去1週間で人気に3記事取得
        popular_list = {res[0].split("/")[2]: res[2] for res in get_10_popular()}
        with open(settings.BASE_DIR+'/blog/data/rank.json', 'w') as fp:
            json.dump(popular_list, fp)


