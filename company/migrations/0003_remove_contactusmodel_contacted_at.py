# Generated by Django 3.2 on 2022-04-13 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_contactusmodel_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactusmodel',
            name='contacted_at',
        ),
    ]
