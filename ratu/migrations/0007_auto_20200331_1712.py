# Generated by Django 2.0.9 on 2020-03-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratu', '0006_auto_20200331_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfop',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='rfop',
            name='kved',
            field=models.CharField(max_length=250),
        ),
    ]
