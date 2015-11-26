# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('owner', models.CharField(help_text='The name of the person doing the reservation', max_length=255)),
                ('start', models.DateTimeField(help_text='When the reservation starts')),
                ('duration', models.DurationField(help_text='How long the reservation lasts')),
            ],
        ),
    ]
