# Generated by Django 5.0.1 on 2024-02-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('name', 'course'), 'verbose_name': 'урок', 'verbose_name_plural': 'уроки'},
        ),
    ]
