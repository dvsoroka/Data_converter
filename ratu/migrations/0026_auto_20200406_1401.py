# Generated by Django 2.0.9 on 2020-04-06 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratu', '0025_kved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruo',
            name='kved',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ratu.Kved'),
            preserve_default=False,
        ),
    ]
