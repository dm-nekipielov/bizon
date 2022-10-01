# Generated by Django 4.1.1 on 2022-10-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0002_product_code"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="product",
            new_name="products",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="category",
            new_name="subcategory",
        ),
        migrations.AlterField(
            model_name="comment",
            name="text",
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="comment",
            name="title",
            field=models.CharField(max_length=128),
        ),
    ]