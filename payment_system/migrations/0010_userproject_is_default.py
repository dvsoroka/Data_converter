# Generated by Django 3.0.7 on 2020-11-13 15:14

from django.db import migrations, models
from django.utils import timezone
from django.conf import settings

import payment_system.models as payment_system_models
from data_ocean.utils import generate_key


def default_projects(apps, schema):
    User = apps.get_model('users', 'DataOceanUser')
    Project = apps.get_model('payment_system', 'Project')
    UserProject = apps.get_model('payment_system', 'UserProject')
    ProjectSubscription = apps.get_model('payment_system', 'ProjectSubscription')
    Subscription = apps.get_model('payment_system', 'Subscription')

    for user in User.objects.all():
        u2p = user.user_projects.filter(role='initiator').first()
        if u2p:
            u2p.is_default = True
            u2p.save()
        else:
            new_project = Project.objects.create(
                name=settings.DEFAULT_PROJECT_NAME,
                description=settings.DEFAULT_PROJECT_DESCRIPTION,
                token=generate_key(),
            )
            UserProject.objects.create(
                project=new_project,
                user=user,
                role='initiator',
                status='active',
                is_default=True,
            )
            def_sub, created = Subscription.objects.get_or_create(
                name=settings.DEFAULT_SUBSCRIPTION_NAME,
                defaults={'requests_limit': 200},
            )
            ProjectSubscription.objects.create(
                project=new_project,
                subscription=def_sub,
                status='active',
                expiring_date=timezone.localdate() + timezone.timedelta(days=30)
            )


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0009_auto_20201112_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='is_default',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.RunPython(
            code=default_projects,
            reverse_code=migrations.RunPython.noop,
        )
    ]
