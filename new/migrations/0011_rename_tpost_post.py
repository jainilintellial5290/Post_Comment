# Generated by Django 3.2.13 on 2022-05-18 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0010_rename_post_tpost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tpost',
            new_name='Post',
        ),
    ]
