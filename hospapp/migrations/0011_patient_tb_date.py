# Generated by Django 4.2.4 on 2023-09-15 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospapp', '0010_book_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_tb',
            name='Date',
            field=models.DateTimeField(auto_now=True, verbose_name='Created'),
        ),
    ]