# Generated by Django 4.0.3 on 2022-04-08 07:44

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0004_auto_20220408_0834"),
    ]

    operations = [
        migrations.AddField(
            model_name="shopuser",
            name="activation_key",
            field=models.CharField(blank=True, max_length=128, verbose_name="ключ подтверждения"),
        ),
        migrations.AddField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 4, 10, 7, 44, 3, 194812, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]
