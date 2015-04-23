# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150422_0657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='review',
            name='food',
        ),
        migrations.RemoveField(
            model_name='review',
            name='gymtype',
        ),
        migrations.RemoveField(
            model_name='review',
            name='outdoor',
        ),
        migrations.RemoveField(
            model_name='review',
            name='outlets',
        ),
        migrations.RemoveField(
            model_name='review',
            name='proshop',
        ),
        migrations.RemoveField(
            model_name='review',
            name='seating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='wifi',
        ),
        migrations.AddField(
            model_name='location',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='gymtype',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Fitness Center'), (2, b'Hardcore Gym Yeah Baby'), (3, b'Bodybuilding'), (4, b'Garage Gym'), (5, b'Powerlifting Gym'), (6, b'You cant be serious')]),
        ),
        migrations.AddField(
            model_name='location',
            name='outdoor',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='outlets',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AddField(
            model_name='location',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='proshop',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='location',
            name='seating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AddField(
            model_name='location',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')]),
        ),
    ]
