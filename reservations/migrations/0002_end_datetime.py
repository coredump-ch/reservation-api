# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('start',)},
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='duration',
        ),
        migrations.AddField(
            model_name='reservation',
            name='end',
            field=models.DateTimeField(help_text='When the reservation ends', default=datetime.datetime(2099, 12, 12, 0, 0, 0, 0, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
