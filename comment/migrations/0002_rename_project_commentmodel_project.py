# Generated by Django 3.2 on 2022-04-13 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='Project',
            new_name='project',
        ),
    ]
