# Generated by Django 5.1.6 on 2025-02-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0004_jobapplication_address_jobapplication_education_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='application_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
