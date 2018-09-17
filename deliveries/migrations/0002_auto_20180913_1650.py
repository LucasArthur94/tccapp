# Generated by Django 2.1 on 2018-09-13 19:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='score',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)]),
        ),
    ]