# Generated by Django 3.0.2 on 2020-10-14 23:54

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20201007_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (3, 'Sci-fi'), (1, 'Horror'), (2, 'Komedia')], default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (3, 'Sci-fi'), (1, 'Horror'), (2, 'Komedia')], default=0),
        ),
        migrations.AddField(
            model_name='serial',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (3, 'Sci-fi'), (1, 'Horror'), (2, 'Komedia')], default=0),
        ),
        migrations.AlterField(
            model_name='anime',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE'), (1, 'HBO'), (5, 'CDA')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE'), (1, 'HBO'), (5, 'CDA')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE'), (1, 'HBO'), (5, 'CDA')], max_length=9, null=True),
        ),
    ]
