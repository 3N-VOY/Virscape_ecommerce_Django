# Generated by Django 4.2.4 on 2023-09-10 22:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_alter_item_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/categories"
            ),
        ),
    ]
