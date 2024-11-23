# Generated by Django 5.1.3 on 2024-11-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uongozini', '0005_remove_post_image_post_image_url_delete_chatmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='uploads/default.jpg', upload_to='uploads/'),
        ),
    ]