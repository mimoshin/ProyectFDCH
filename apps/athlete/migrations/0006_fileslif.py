# Generated by Django 3.1.7 on 2021-10-27 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0005_auto_20211027_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileslif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.CharField(max_length=200)),
                ('texto', models.CharField(max_length=100000)),
            ],
        ),
    ]
