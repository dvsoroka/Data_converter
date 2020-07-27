# Generated by Django 3.0.7 on 2020-07-24 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_ocean', '0005_auto_20200722_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authority',
            options={'verbose_name': 'орган реєстрації'},
        ),
        migrations.AlterModelOptions(
            name='register',
            options={'verbose_name': 'реєстр'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'статус'},
        ),
        migrations.AlterModelOptions(
            name='taxpayertype',
            options={'verbose_name': 'тип платника податків'},
        ),
        migrations.AlterField(
            model_name='authority',
            name='code',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='код ЄДРПОУ'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='name',
            field=models.CharField(max_length=500, unique=True, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='register',
            name='data_ocean_list',
            field=models.URLField(max_length=500, verbose_name='отримати списком'),
        ),
        migrations.AlterField(
            model_name='register',
            name='data_ocean_retrieve',
            field=models.URLField(max_length=500, verbose_name="отримати об'єкт"),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=500, unique=True, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='register',
            name='source_last_update',
            field=models.DateTimeField(default=None, null=True, verbose_name='востаннє оновлено'),
        ),
        migrations.AlterField(
            model_name='register',
            name='source_name',
            field=models.CharField(max_length=300, verbose_name='назва джерела даних'),
        ),
        migrations.AlterField(
            model_name='register',
            name='source_register_id',
            field=models.CharField(max_length=36, unique=True, verbose_name='ID реєстру у джерелі даних'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='taxpayertype',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='назва'),
        ),
    ]
