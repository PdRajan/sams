# Generated by Django 5.0.4 on 2024-05-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="honors",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="patent",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="publication",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="researchproject",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
    ]