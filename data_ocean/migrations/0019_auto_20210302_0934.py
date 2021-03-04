# Generated by Django 3.0.7 on 2021-03-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_ocean', '0018_auto_20210215_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='registryupdatermodel',
            name='errors',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='registryupdatermodel',
            name='records_added',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='registryupdatermodel',
            name='records_changed',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='registryupdatermodel',
            name='records_deleted',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
