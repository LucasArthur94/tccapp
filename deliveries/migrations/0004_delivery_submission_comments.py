# Generated by Django 2.1.2 on 2018-11-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0003_auto_20180913_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='submission_comments',
            field=models.TextField(default='', max_length=500),
        ),
    ]
