# Generated by Django 4.2.4 on 2023-09-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospapp', '0013_book_appointment_date_book_appointment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_appointment',
            name='Date',
            field=models.DateTimeField(auto_now=True, verbose_name='Created'),
        ),
    ]
