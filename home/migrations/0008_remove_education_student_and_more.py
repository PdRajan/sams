# Generated by Django 5.0.4 on 2024-05-23 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_experience_approved_by_experience_is_approved_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="education",
            name="student",
        ),
        migrations.RemoveField(
            model_name="experience",
            name="approved_by",
        ),
        migrations.RemoveField(
            model_name="experience",
            name="student",
        ),
        migrations.RemoveField(
            model_name="honors",
            name="approved_by",
        ),
        migrations.RemoveField(
            model_name="honors",
            name="student",
        ),
        migrations.RemoveField(
            model_name="patent",
            name="approved_by",
        ),
        migrations.RemoveField(
            model_name="patent",
            name="student",
        ),
        migrations.RemoveField(
            model_name="publication",
            name="approved_by",
        ),
        migrations.RemoveField(
            model_name="publication",
            name="student",
        ),
        migrations.RemoveField(
            model_name="researchproject",
            name="approved_by",
        ),
        migrations.RemoveField(
            model_name="researchproject",
            name="student",
        ),
        migrations.RemoveField(
            model_name="studentachievement",
            name="approved_by",
        ),
        migrations.RemoveField(
            model_name="studentachievement",
            name="student",
        ),
        migrations.DeleteModel(
            name="Committee_membership",
        ),
        migrations.DeleteModel(
            name="Education",
        ),
        migrations.DeleteModel(
            name="Experience",
        ),
        migrations.DeleteModel(
            name="Honors",
        ),
        migrations.DeleteModel(
            name="Patent",
        ),
        migrations.DeleteModel(
            name="Publication",
        ),
        migrations.DeleteModel(
            name="ResearchProject",
        ),
        migrations.DeleteModel(
            name="StudentAchievement",
        ),
    ]
