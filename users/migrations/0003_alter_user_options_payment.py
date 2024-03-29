# Generated by Django 5.0.1 on 2024-02-13 03:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_course_lms_course_name_be59f6_idx'),
        ('users', '0002_remove_user_username_user_avatar_user_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateField(verbose_name='дата платежа')),
                ('amount_payment', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма оплаты')),
                ('method_payment', models.CharField(choices=[('cash', 'наличными'), ('card', 'картой')], max_length=10, verbose_name='метод оплаты')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='оплаченный курс')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]
