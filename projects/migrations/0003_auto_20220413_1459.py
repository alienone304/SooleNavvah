# Generated by Django 3.2 on 2022-04-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220413_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsmodel',
            name='height',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='length',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='width',
            field=models.CharField(max_length=264),
        ),
    ]
