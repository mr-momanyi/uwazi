# Generated by Django 5.1.3 on 2024-11-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uongozini', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='uploads/default.jpg', upload_to='uploads/'),
        ),
    ]