# Generated by Django 3.2.9 on 2022-04-23 18:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0011_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 25, 18, 37, 2, 137614, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
