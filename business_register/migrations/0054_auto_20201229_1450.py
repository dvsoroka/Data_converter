# Generated by Django 3.0.7 on 2020-12-29 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0053_relatedpersonslink_relationship_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relatedpersonslink',
            old_name='relationship_category',
            new_name='category',
        ),
    ]
