# Generated by Django 5.0.4 on 2024-05-22 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_faculty_address_faculty_contact_number_faculty_dob_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="faculty",
            name="gender",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
