"""python manage.py execute で呼ぶ処理を定義するモジュール."""
from django.core.management.base import BaseCommand
from .HelloAnalytics import get_10_popular


class Command(BaseCommand):
    """コマンド定義のためのクラス."""

    def handle(self, *args, **options):
        """コマンド定義のための関数。実際の処理はapi.main()."""
        # 過去一週間の人気データを全て削除し、新たに作り直す
        for url, title, page_view in get_10_popular():
            print(url)
            print(title)
            print(page_view)
