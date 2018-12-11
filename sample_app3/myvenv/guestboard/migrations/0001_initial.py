# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名前', max_length=64, help_text='あなたの名前を入力してください')),
                ('message', models.CharField(verbose_name='メッセージ', max_length=255, help_text='メッセージを入力してください')),
                ('created_at', models.DateTimeField(verbose_name='登録日時', auto_now_add=True)),
            ],
        ),
    ]
