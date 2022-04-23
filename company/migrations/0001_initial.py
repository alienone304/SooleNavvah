# Generated by Django 3.2 on 2022-04-01 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=264, null=True)),
                ('request', models.TextField(blank=True, null=True)),
                ('contacted_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
