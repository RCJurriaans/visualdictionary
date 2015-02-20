# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualwords', '0003_auto_20150218_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualword',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visualword',
            name='nsfw',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
