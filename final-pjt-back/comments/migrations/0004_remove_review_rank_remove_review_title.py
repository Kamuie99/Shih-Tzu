# Generated by Django 4.2.8 on 2024-05-19 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_rename_movie_id_review_movie_alter_comment_review_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
    ]