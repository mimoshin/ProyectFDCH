# Generated by Django 3.1.7 on 2021-10-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0003_auto_20211026_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athletes',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]