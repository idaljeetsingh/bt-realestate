# Generated by Django 2.2.7 on 2019-12-20 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2019, 12, 20, 13, 44, 10, 414724)),
        ),
    ]
