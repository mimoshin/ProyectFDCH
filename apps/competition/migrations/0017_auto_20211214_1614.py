# Generated by Django 3.1.7 on 2021-12-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0016_jumpassignments_competititonnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='midassignments',
            name='competititonNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='throwassignments',
            name='competititonNumber',
            field=models.IntegerField(default=0),
        ),
    ]
