# Generated by Django 3.2.19 on 2023-06-11 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_filter',
        ),
    ]