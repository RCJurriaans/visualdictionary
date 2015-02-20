# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualwords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualword',
            name='url_raw',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visualword',
            name='url_thumb',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
