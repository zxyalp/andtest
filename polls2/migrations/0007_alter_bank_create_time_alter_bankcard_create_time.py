# Generated by Django 4.0.2 on 2022-02-19 12:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls2', '0006_alter_bank_create_time_alter_bankcard_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bankcard',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
