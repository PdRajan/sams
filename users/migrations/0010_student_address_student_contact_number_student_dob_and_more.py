# Generated by Django 5.0.6 on 2024-05-24 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_student_expertise'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]