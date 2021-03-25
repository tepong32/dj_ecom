# Generated by Django 2.1 on 2021-03-11 16:54

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.Product.image_directory_path),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]