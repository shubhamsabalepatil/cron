# Generated by Django 4.1.4 on 2023-01-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0004_alter_instance_status2_start_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance_status2',
            name='stop_datetime',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='instance_status2',
            name='start_datetime',
            field=models.DateTimeField(),
        ),
    ]
