# Generated by Django 5.0.8 on 2024-08-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='no img.png', upload_to=''),
        ),
    ]
