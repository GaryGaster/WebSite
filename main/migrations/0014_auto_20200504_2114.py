# Generated by Django 3.0.2 on 2020-05-04 21:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200425_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (1, 'HBO'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (1, 'HBO'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (1, 'HBO'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='xvideo',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (1, 'HBO'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
    ]
