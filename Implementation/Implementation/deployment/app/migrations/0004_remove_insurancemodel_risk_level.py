# Generated by Django 3.2 on 2022-04-08 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_insurancemodel_risk_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurancemodel',
            name='risk_level',
        ),
    ]
