# Generated by Django 5.0.8 on 2024-08-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='media/images/banner.jpg', upload_to=''),
        ),
    ]
