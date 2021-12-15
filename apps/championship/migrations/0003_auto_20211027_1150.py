# Generated by Django 3.1.7 on 2021-10-27 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0002_auto_20211025_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='championships',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='championships',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='championships',
            name='category',
            field=models.CharField(default='000001000', max_length=9),
        ),
    ]