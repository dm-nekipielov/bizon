# Generated by Django 4.1.1 on 2022-09-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="code",
            field=models.IntegerField(null=True),
        ),
    ]
