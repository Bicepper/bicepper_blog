# Generated by Django 2.2.1 on 2019-06-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190602_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='mainimage/', verbose_name='サムネイル画像'),
        ),
    ]
