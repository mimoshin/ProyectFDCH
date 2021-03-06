# Generated by Django 3.1.7 on 2021-11-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0012_competitions_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='inscriptions',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='jumpassignments',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='jumpheats',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='jumpparticipation',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='midassignments',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='midheats',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='speedassignments',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='speedheats',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='throwassignments',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='throwheats',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
        migrations.AddField(
            model_name='throwparticipation',
            name='status',
            field=models.IntegerField(choices=[(0, 'DEFAULT'), (1, 'ACTIVO'), (2, 'REALIZADO'), (3, 'SUSPENDIDO'), (4, 'APLAZADO'), (5, 'DESACTIVADO')], default=1),
        ),
    ]
