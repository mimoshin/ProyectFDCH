# Generated by Django 3.1.7 on 2021-11-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0006_auto_20211027_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscriptions',
            name='strAthle',
            field=models.CharField(default='PIVOTE', max_length=200),
        ),
    ]
