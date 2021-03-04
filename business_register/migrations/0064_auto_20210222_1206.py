# Generated by Django 3.0.7 on 2021-02-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0063_auto_20210215_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpep',
            name='fullname_transcriptions_eng',
            field=models.TextField(db_index=True, verbose_name='options for writing the full name'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='last_employer',
            field=models.CharField(db_index=True, max_length=512, null=True, verbose_name='last office'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='last_job_title',
            field=models.CharField(db_index=True, max_length=340, null=True, verbose_name='last position'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='pep_type',
            field=models.CharField(blank=True, choices=[('national PEP', 'National politically exposed person'), ('foreign PEP', 'Foreign politically exposed person'), ('PEP with political functions in international organization', 'Politically exposed person, having political functions in international organization'), ('associated person with PEP', 'Associated person'), ('member of PEP`s family', 'Family member')], db_index=True, max_length=60, null=True, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='fullname_transcriptions_eng',
            field=models.TextField(db_index=True, verbose_name='options for writing the full name'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='last_employer',
            field=models.CharField(db_index=True, max_length=512, null=True, verbose_name='last office'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='last_job_title',
            field=models.CharField(db_index=True, max_length=340, null=True, verbose_name='last position'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='pep_type',
            field=models.CharField(blank=True, choices=[('national PEP', 'National politically exposed person'), ('foreign PEP', 'Foreign politically exposed person'), ('PEP with political functions in international organization', 'Politically exposed person, having political functions in international organization'), ('associated person with PEP', 'Associated person'), ('member of PEP`s family', 'Family member')], db_index=True, max_length=60, null=True, verbose_name='type'),
        ),
    ]
