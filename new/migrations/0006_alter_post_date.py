# Generated by Django 3.2.13 on 2022-05-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0005_auto_20220518_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]