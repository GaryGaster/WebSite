# Generated by Django 3.0.2 on 2020-03-30 22:56

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200330_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(blank=True, default='video-default.jpeg', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (3, 'AMAZONPRIME'), (2, 'NETFLIX'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, default='video-default.jpeg', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (3, 'AMAZONPRIME'), (2, 'NETFLIX'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='image',
            field=models.ImageField(blank=True, default='video-default.jpeg', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='serial',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (3, 'AMAZONPRIME'), (2, 'NETFLIX'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='xvideo',
            name='image',
            field=models.ImageField(blank=True, default='video-default.jpeg', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='xvideo',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (3, 'AMAZONPRIME'), (2, 'NETFLIX'), (4, 'YOUTUBE')], max_length=7, null=True),
        ),
    ]
