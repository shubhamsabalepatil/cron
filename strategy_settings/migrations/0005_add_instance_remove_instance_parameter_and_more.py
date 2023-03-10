# Generated by Django 4.1.4 on 2023-01-05 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strategy_settings', '0004_sample_delete_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Instance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exchange', models.CharField(choices=[('NSE', 'NSE'), ('BSE', 'BSE')], max_length=30)),
                ('Symbol', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30)),
                ('is_Monday', models.BooleanField(default=False, verbose_name='Monday')),
                ('is_Tuesday', models.BooleanField(default=False, verbose_name='Tuesday')),
                ('is_Wednesday', models.BooleanField(default=False, verbose_name='Wednesday')),
                ('is_Thursday', models.BooleanField(default=False, verbose_name='Thursday')),
                ('is_Friday', models.BooleanField(default=False, verbose_name='Friday')),
                ('Initialize_Time', models.TimeField()),
                ('Terminate_Time', models.TimeField()),
                ('Strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy_settings.strategy_details')),
            ],
        ),
        migrations.RemoveField(
            model_name='instance',
            name='Parameter',
        ),
        migrations.RemoveField(
            model_name='instance',
            name='Strategy',
        ),
        migrations.RemoveField(
            model_name='instance',
            name='Symbol',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
        migrations.DeleteModel(
            name='Instance',
        ),
    ]
