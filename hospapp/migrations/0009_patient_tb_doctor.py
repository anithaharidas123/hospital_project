# Generated by Django 4.2.4 on 2023-09-13 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospapp', '0008_rename_patient_patient_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_tb',
            name='DOCTOR',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
