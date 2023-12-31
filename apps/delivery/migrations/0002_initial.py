# Generated by Django 4.2.4 on 2023-09-30 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("delivery", "0001_initial"),
        ("clients", "0001_initial"),
        ("surveys", "0001_initial"),
        ("companies", "0001_initial"),
        ("operations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="surveydeliveryconfig",
            name="survey",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="surveys.survey"
            ),
        ),
        migrations.AddField(
            model_name="deliveryrecord",
            name="client",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="clients.client"),
        ),
        migrations.AddField(
            model_name="deliveryrecord",
            name="config",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="delivery.surveydeliveryconfig"),
        ),
        migrations.AddField(
            model_name="deliveryrecord",
            name="operation_type",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="operations.operationtype"
            ),
        ),
        migrations.AddField(
            model_name="deliveryinterval",
            name="brand",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="companies.brand"),
        ),
        migrations.AddField(
            model_name="deliveryconfig",
            name="brand",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="companies.brand"),
        ),
        migrations.AddField(
            model_name="deliveryconfig",
            name="content_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="delivery.deliverycontenttemplate",
            ),
        ),
        migrations.AddField(
            model_name="deliveryconfig",
            name="operation_type",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="operations.operationtype"
            ),
        ),
        migrations.AddField(
            model_name="deliveryconfig",
            name="survey",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="surveys.survey"),
        ),
    ]
