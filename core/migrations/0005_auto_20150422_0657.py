# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='review',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='review',
            name='gymtype',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Fitness Center'), (2, b'Hardcore Gym Yeah Baby'), (3, b'Bodybuilding'), (4, b'Garage Gym'), (5, b'Powerlifting Gym'), (6, b'You cant be serious')]),
        ),
        migrations.AddField(
            model_name='review',
            name='outdoor',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='review',
            name='outlets',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AddField(
            model_name='review',
            name='proshop',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='review',
            name='seating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
        ),
        migrations.AddField(
            model_name='review',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')]),
        ),
    ]
