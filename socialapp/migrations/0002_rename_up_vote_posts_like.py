# Generated by Django 4.1.1 on 2022-11-08 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='up_vote',
            new_name='like',
        ),
    ]
