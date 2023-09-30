# Generated by Django 4.2.4 on 2023-09-30 06:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("delivery", "0001_initial"),
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("hash_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("description", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_public", models.BooleanField(default=False)),
                ("is_anonymous", models.BooleanField(default=False)),
                ("texto1", models.TextField(blank=True, null=True)),
                ("texto2", models.TextField(blank=True, null=True)),
                ("brand", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="companies.brand")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SurveyType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_public", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SurveyQuestion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "question_text",
                    models.CharField(
                        help_text="Puedes añadir variables con {{variable}} ex: {{componente}} {{atributo}}",
                        max_length=255,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("info", "info"),
                            ("enps", "enps"),
                            ("components", "componentes"),
                            ("attributes", "attributes"),
                            ("text", "text"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "enps_filter",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("-", None),
                            ("detractors", "detractors"),
                            ("neutrals", "neutrals"),
                            ("promoters", "promoters"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("order", models.IntegerField()),
                ("is_required", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("answer_order_related", models.IntegerField(blank=True, null=True)),
                (
                    "attributes",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Selecciona los attributos que quieres que aparezcan en la pregunta, si no está seleccionado el tipo correcto no surgira efecto",
                        to="companies.attribute",
                    ),
                ),
                (
                    "components",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Selecciona los componentes que quieres que aparezcan en la pregunta, si no está seleccionado el tipo correcto no surgira efecto",
                        to="companies.component",
                    ),
                ),
                ("survey", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="surveys.survey")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SurveyAnswer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("value", models.TextField(blank=True, null=True)),
                ("is_anonymous", models.BooleanField(default=False)),
                ("is_enps_filtered", models.BooleanField(default=False)),
                (
                    "enps_profile",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("-", None),
                            ("detractors", "detractors"),
                            ("neutrals", "neutrals"),
                            ("promoters", "promoters"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("extra_data", models.JSONField(blank=True, null=True)),
                ("answer_order", models.IntegerField(blank=True, null=True)),
                (
                    "delivery_config",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="delivery.surveydeliveryconfig",
                    ),
                ),
                (
                    "delivery_record",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="delivery.deliveryrecord"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="surveys.surveyquestion"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
