# Generated by Django 3.2.13 on 2022-05-17 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=models.CharField(max_length=40),
        ),
    ]
