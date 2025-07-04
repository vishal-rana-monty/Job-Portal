# Generated by Django 5.1.6 on 2025-04-10 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_established_year'),
        ('jobs', '0008_job_company_alter_job_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='company.company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience_required',
            field=models.CharField(choices=[('0-2', '0-2 Years'), ('2-4', '2-4 Years'), ('4-6', '4-6 Years'), ('6-8', '6-8 Years'), ('8+', '8+ Years')], help_text='Experience in years', max_length=200),
        ),
    ]
