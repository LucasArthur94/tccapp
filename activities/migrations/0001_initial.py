# Generated by Django 2.1 on 2018-09-04 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplines', '0002_auto_20180903_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField(default=1)),
                ('due_date', models.DateField(default=datetime.date.today)),
                ('main_file_name', models.CharField(default='Documento Principal', max_length=100)),
                ('main_file_required', models.BooleanField(default=False)),
                ('side_file_name', models.CharField(default='Documento Extra', max_length=100)),
                ('side_file_required', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplines.Discipline')),
            ],
        ),
    ]
