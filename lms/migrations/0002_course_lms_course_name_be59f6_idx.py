# Generated by Django 5.0.1 on 2024-02-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['name'], name='lms_course_name_be59f6_idx'),
        ),
    ]
