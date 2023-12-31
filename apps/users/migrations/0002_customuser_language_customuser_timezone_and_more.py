# Generated by Django 4.2.4 on 2023-09-29 09:40

import apps.users.helpers
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="language",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="timezone",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.FileField(
                blank=True, upload_to="profile-pictures/", validators=[apps.users.helpers.validate_profile_picture]
            ),
        ),
    ]
