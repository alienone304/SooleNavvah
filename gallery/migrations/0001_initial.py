# Generated by Django 3.2 on 2022-04-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='gallery/default/default.jpg', upload_to='gallery/')),
                ('description', models.TextField(blank=True, null=True)),
                ('for_project', models.BooleanField(default=False)),
                ('for_factory', models.BooleanField(default=False)),
                ('for_workers', models.BooleanField(default=False)),
                ('for_sundry', models.BooleanField(default=False)),
                ('for_excebition', models.BooleanField(default=False)),
            ],
        ),
    ]
