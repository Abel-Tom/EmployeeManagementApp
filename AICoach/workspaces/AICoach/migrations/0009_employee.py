# Generated by Django 4.2.11 on 2024-04-02 14:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appauth', '0006_appusermodel_app_objects'),
        ('dynamic_models', '0008_recipe_attributes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_joining', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], max_length=10)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('years_of_experience', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
