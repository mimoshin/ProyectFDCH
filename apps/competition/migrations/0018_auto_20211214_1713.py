# Generated by Django 3.1.7 on 2021-12-14 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0017_auto_20211214_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jumpassignments',
            old_name='competititonNumber',
            new_name='competitionNumber',
        ),
        migrations.RenameField(
            model_name='midassignments',
            old_name='competititonNumber',
            new_name='competitionNumber',
        ),
        migrations.RenameField(
            model_name='throwassignments',
            old_name='competititonNumber',
            new_name='competitionNumber',
        ),
    ]