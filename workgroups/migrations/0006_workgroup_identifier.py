# Generated by Django 2.1.2 on 2018-10-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workgroups', '0005_workgroup_modality'),
    ]

    operations = [
        migrations.AddField(
            model_name='workgroup',
            name='identifier',
            field=models.IntegerField(default=1),
        ),
    ]