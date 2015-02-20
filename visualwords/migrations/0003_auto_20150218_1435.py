# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('visualwords', '0002_auto_20150218_1348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visualword',
            options={'ordering': ['word']},
        ),
        migrations.AddField(
            model_name='visualword',
            name='uploaded_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 18, 14, 35, 55, 984697, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
