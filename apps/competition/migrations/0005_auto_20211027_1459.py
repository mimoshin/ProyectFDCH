# Generated by Django 3.1.7 on 2021-10-27 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0004_auto_20211027_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jumpparticipation',
            name='assignmentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigneds', to='competition.jumpassignments'),
        ),
    ]
