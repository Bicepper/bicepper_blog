# Generated by Django 2.2.1 on 2019-10-22 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementblogfooter',
            name='category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='blog.SubCategory', verbose_name='表示カテゴリー'),
        ),
    ]
