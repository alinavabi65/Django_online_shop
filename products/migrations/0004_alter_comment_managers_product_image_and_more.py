# Generated by Django 4.0.2 on 2022-10-08 20:16

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('active_comments_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_cover', verbose_name='Product_Image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='Comment text'),
        ),
    ]
