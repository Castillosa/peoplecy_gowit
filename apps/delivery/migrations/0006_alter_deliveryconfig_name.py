# Generated by Django 4.2.4 on 2023-10-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("delivery", "0005_alter_deliveryconfig_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deliveryconfig",
            name="name",
            field=models.CharField(default="not named", max_length=100),
            preserve_default=False,
        ),
    ]
