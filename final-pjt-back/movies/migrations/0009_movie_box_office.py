# Generated by Django 4.2.8 on 2024-05-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_movie_poster_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='box_office',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
