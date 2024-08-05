# Generated by Django 4.2.14 on 2024-07-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0002_gallery_image_alter_gallery_created_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="作成日"),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="image",
            field=models.ImageField(null=True, upload_to="media/images/"),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="updated_date",
            field=models.DateTimeField(auto_now=True, verbose_name="更新日"),
        ),
    ]
