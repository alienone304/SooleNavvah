# Generated by Django 3.2.13 on 2022-04-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_famouscustomermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famouscustomermodel',
            name='picture',
            field=models.ImageField(default='comment/default/default.jpg', upload_to='comment/logos/'),
        ),
    ]
