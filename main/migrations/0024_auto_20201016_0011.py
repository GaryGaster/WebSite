# Generated by Django 3.0.2 on 2020-10-16 00:11

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20201015_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (2, 'Komedia'), (0, 'Inne'), (3, 'Sci-fi')], default=0),
        ),
        migrations.AlterField(
            model_name='anime',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(4, 'YOUTUBE'), (3, 'AMAZONPRIME'), (5, 'CDA'), (2, 'NETFLIX'), (1, 'HBO')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (2, 'Komedia'), (0, 'Inne'), (3, 'Sci-fi')], default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(4, 'YOUTUBE'), (3, 'AMAZONPRIME'), (5, 'CDA'), (2, 'NETFLIX'), (1, 'HBO')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (2, 'Komedia'), (0, 'Inne'), (3, 'Sci-fi')], default=0),
        ),
        migrations.AlterField(
            model_name='serial',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(4, 'YOUTUBE'), (3, 'AMAZONPRIME'), (5, 'CDA'), (2, 'NETFLIX'), (1, 'HBO')], max_length=9, null=True),
        ),
        migrations.CreateModel(
            name='SerialRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(default='')),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Serial')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(default='')),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Anime')),
            ],
        ),
    ]
