# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualwords', '0004_auto_20150218_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visualword',
            old_name='url',
            new_name='url_img',
        ),
    ]
