# Generated by Django 2.1 on 2021-03-10 13:08

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210226_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/round.png', help_text='Help us recognize you. ;)', upload_to=user.models.Profile.dp_directory_path, verbose_name='Profile Picture: '),
        ),
    ]