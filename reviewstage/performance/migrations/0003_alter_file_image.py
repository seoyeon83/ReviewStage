# Generated by Django 4.2.11 on 2024-04-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_rename_likes_count_review_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image/'),
        ),
    ]
