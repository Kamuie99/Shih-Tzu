# Generated by Django 4.2.8 on 2024-05-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_runtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='belongs_to_collection',
            field=models.JSONField(null=True),
        ),
    ]
