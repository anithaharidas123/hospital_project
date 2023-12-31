# Generated by Django 4.2.4 on 2023-09-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospapp', '0016_discharge_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_appointment',
            name='patient_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='discharge_tb',
            name='patient_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient_tb',
            name='patient_id',
            field=models.IntegerField(default=0),
        ),
    ]
