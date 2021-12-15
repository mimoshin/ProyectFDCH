# Generated by Django 3.1.7 on 2021-10-25 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athletes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='FIRSTNAME', max_length=200)),
                ('secondName', models.CharField(default='SECONNAME', max_length=200)),
                ('surname', models.CharField(default='SURNAME', max_length=200)),
                ('secondSurname', models.CharField(default='sSURNAME', max_length=200)),
                ('rut', models.CharField(default='RUT', max_length=200)),
                ('gender', models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'DAMAS'), (2, 'VARONES')], default=0)),
                ('clubId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.clubs')),
            ],
        ),
    ]
