# Generated by Django 2.2.1 on 2019-06-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190606_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]