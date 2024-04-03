# Generated by Django 4.2.11 on 2024-04-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0009_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='time_off_days',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], max_length=12),
        ),
    ]
