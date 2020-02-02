# Generated by Django 3.0.2 on 2020-02-02 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(3, 'AMAZONPRIME'), (2, 'NETFLIX'), (1, 'HBO')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(3, 'AMAZONPRIME'), (2, 'NETFLIX'), (1, 'HBO')], max_length=5, null=True),
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('platforms', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(3, 'AMAZONPRIME'), (2, 'NETFLIX'), (1, 'HBO')], max_length=5, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('votes_total', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media/')),
                ('url', models.CharField(blank=True, max_length=600, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voters', models.ManyToManyField(related_name='anime_voters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
