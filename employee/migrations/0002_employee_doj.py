# Generated by Django 3.2.12 on 2023-11-24 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='doj',
            field=models.DateField(default=datetime.date(2023, 11, 24)),
            preserve_default=False,
        ),
    ]