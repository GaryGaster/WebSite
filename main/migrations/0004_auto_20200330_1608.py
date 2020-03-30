# Generated by Django 3.0.2 on 2020-03-30 16:08

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200320_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='serial',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='xvideo',
            name='likes',
        ),
        migrations.AlterField(
            model_name='anime',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='xvideo',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
    ]