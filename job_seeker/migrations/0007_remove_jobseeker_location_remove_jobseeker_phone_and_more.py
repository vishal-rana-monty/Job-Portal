# Generated by Django 5.1.6 on 2025-03-03 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0006_jobapplication_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='location',
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='phone',
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='contact_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='education',
            field=models.TextField(default='Not Provided'),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='skills',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
