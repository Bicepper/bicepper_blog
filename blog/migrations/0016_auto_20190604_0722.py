# Generated by Django 2.2.1 on 2019-06-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_blogpost_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリ名')),
            ],
            options={
                'verbose_name': 'カテゴリ',
                'verbose_name_plural': 'カテゴリ',
            },
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='is_public',
            field=models.BooleanField(default=False, help_text='非公開にする場合はチェックを入れる', verbose_name='非公開設定'),
        ),
    ]
