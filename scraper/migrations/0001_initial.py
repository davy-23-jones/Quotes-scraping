# Generated by Django 5.0.2 on 2024-02-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scrape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
            ],
        ),
    ]
