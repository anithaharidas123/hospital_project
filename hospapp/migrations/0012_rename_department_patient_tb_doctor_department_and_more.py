# Generated by Django 4.2.4 on 2023-09-15 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospapp', '0011_patient_tb_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_tb',
            old_name='DEPARTMENT',
            new_name='DOCTOR_DEPARTMENT',
        ),
        migrations.RemoveField(
            model_name='patient_tb',
            name='DOCTOR',
        ),
    ]
