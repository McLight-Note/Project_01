# Generated by Django 5.2.3 on 2025-06-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("remProd", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="id",
        ),
        migrations.AddField(
            model_name="product",
            name="product_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
