# Generated by Django 3.1.1 on 2020-12-03 15:04

from django.db import migrations
from django.contrib.auth.models import Group, Permission


def populate_permissions(apps, schema_editor):
    ''' Add default archivist staff '''
    group = Group.objects.get(name='archivist_user')

    existing_permissions = group.permissions.all()

    for codename in (
        # Bag
        'change_bag',
        'view_bag',
        # Job
        'add_job',
        'change_job',
        'view_job',
        # UploadedFile
        'view_uploadedfile',
        # UploadSession
        'view_uploadsession',
        # User
        'add_user',
        'change_user',
        'view_user'):
        permission = Permission.objects.get(codename=codename)
        if permission not in existing_permissions:
            group.permissions.add(permission)


class Migration(migrations.Migration):

    dependencies = [
        ('recordtransfer', '0010_update_site_name'),
    ]

    operations = [
        migrations.RunPython(populate_permissions)
    ]
