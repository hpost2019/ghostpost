# Generated by Django 3.1 on 2020-08-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20200821_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='boast',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='down_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='up_votes',
            field=models.IntegerField(default=0),
        ),
    ]