# Generated by Django 2.2.1 on 2019-06-02 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190602_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日'),
        ),
    ]
