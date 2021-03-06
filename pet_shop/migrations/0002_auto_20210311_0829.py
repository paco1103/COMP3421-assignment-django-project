# Generated by Django 3.0.8 on 2021-03-11 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='adopt',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adopt_date', models.DateTimeField(auto_now_add=True)),
                ('pet_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pet_shop.Pet')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['adopt_date'],
            },
        ),
    ]
