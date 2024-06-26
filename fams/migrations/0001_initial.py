# Generated by Django 5.0.4 on 2024-05-12 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0003_faculty_department"),
    ]

    operations = [
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("school", models.CharField(max_length=225)),
                ("degree", models.CharField(max_length=225)),
                ("field_of_study", models.CharField(max_length=225)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("grade", models.CharField(max_length=10)),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="educations",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("employment_type", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=225)),
                ("location", models.CharField(max_length=225)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField()),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="experiences",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Publication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=225)),
                ("issuing_organization", models.CharField(max_length=225)),
                ("issue_date", models.DateField()),
                ("expiration_date", models.DateField()),
                ("credential_id", models.CharField(max_length=225)),
                ("credential_url", models.URLField()),
                ("file", models.FileField(upload_to="publications/")),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="publications",
                        to="users.faculty",
                    ),
                ),
            ],
        ),
    ]
