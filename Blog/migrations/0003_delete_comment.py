# Generated by Django 4.0.5 on 2022-09-09 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_categories_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
