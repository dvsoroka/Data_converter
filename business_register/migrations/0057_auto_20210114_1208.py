# Generated by Django 3.0.7 on 2021-01-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0056_merge_20210112_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='source',
            field=models.CharField(blank=True, choices=[('ukr', 'Єдиний державний реєстр юридичних осіб, фізичних осіб – підприємців та громадських формувань України'), ('gb', 'Companies House'), ('antac', 'Центр протидії корупції')], default=None, max_length=5, null=True, verbose_name='джерело даних'),
        ),
        migrations.AddField(
            model_name='historicalcompany',
            name='source',
            field=models.CharField(blank=True, choices=[('ukr', 'Єдиний державний реєстр юридичних осіб, фізичних осіб – підприємців та громадських формувань України'), ('gb', 'Companies House'), ('antac', 'Центр протидії корупції')], default=None, max_length=5, null=True, verbose_name='джерело даних'),
        ),
    ]
