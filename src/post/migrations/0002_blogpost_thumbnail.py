# Generated by Django 3.1.7 on 2023-03-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
