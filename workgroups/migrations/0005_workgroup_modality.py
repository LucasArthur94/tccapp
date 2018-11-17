# Generated by Django 2.1.2 on 2018-10-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workgroups', '0004_auto_20180906_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='workgroup',
            name='modality',
            field=models.CharField(choices=[('SMS', 'Semestral'), ('QDR', 'Quadrimestral')], default='QDR', max_length=3),
        ),
    ]