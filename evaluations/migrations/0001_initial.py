# Generated by Django 2.1.2 on 2018-11-16 14:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('allocations', '0002_auto_20181112_1824'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation_for_best_project', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('presentation', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)])),
                ('arguing', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)])),
                ('implementation', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)])),
                ('documentation', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)])),
                ('private_comments', models.TextField(default='', max_length=500)),
                ('needs_fixes', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('allocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allocations.Allocation')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
