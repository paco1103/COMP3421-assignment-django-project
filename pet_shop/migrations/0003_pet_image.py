# Generated by Django 3.0.8 on 2021-03-11 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_shop', '0002_auto_20210311_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
