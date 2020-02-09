# Generated by Django 3.0.2 on 2020-02-09 23:04

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200209_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (1, 'HBO'), (3, 'AMAZONPRIME')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (1, 'HBO'), (3, 'AMAZONPRIME')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (1, 'HBO'), (3, 'AMAZONPRIME')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='xvideo',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (1, 'HBO'), (3, 'AMAZONPRIME')], max_length=5, null=True),
        ),
    ]
