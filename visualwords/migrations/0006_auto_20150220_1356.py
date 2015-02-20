# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualwords', '0005_auto_20150218_1956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visualword',
            options={'ordering': ['word', 'uploaded_on']},
        ),
        migrations.AddField(
            model_name='visualword',
            name='url_animated',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
