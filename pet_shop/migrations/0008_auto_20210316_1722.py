# Generated by Django 3.0.8 on 2021-03-16 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_shop', '0007_auto_20210316_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='birth',
            field=models.DateField(default=datetime.datetime(2021, 3, 16, 17, 22, 6, 807858), help_text='Enter pet birth'),
        ),
    ]