# Generated by Django 3.1.7 on 2021-11-15 20:44

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asociationadmin',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='asociationadmin',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='asociationadmin',
            name='id',
        ),
        migrations.RemoveField(
            model_name='asociationadmin',
            name='logUser',
        ),
        migrations.AddField(
            model_name='asociationadmin',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user'),
            preserve_default=False,
        ),
    ]
