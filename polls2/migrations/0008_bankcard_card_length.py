# Generated by Django 4.0.2 on 2022-02-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls2', '0007_alter_bank_create_time_alter_bankcard_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankcard',
            name='card_length',
            field=models.IntegerField(null=True),
        ),
    ]
