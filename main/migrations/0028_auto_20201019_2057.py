# Generated by Django 3.0.2 on 2020-10-19 20:57

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20201018_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='date_of_birth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Komedia'), (1, 'Horror'), (0, 'Inne'), (3, 'Sci-fi')], default=0),
        ),
        migrations.AlterField(
            model_name='anime',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(5, 'CDA'), (1, 'HBO'), (2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Komedia'), (1, 'Horror'), (0, 'Inne'), (3, 'Sci-fi')], default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(5, 'CDA'), (1, 'HBO'), (2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Komedia'), (1, 'Horror'), (0, 'Inne'), (3, 'Sci-fi')], default=0),
        ),
        migrations.AlterField(
            model_name='serial',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(5, 'CDA'), (1, 'HBO'), (2, 'NETFLIX'), (3, 'AMAZONPRIME'), (4, 'YOUTUBE')], max_length=9, null=True),
        ),
    ]
