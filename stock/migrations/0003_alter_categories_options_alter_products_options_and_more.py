# Generated by Django 4.2.6 on 2023-10-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_categories_remove_products_size_products_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='products',
            name='picture',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
