# Generated by Django 3.1.1 on 2020-09-15 15:07
# Edited manually by Daniel Lovegrove
import logging

from django.db import models, migrations
from django.contrib.auth.models import Group

LOGGER = logging.getLogger(__name__)


def create_groups(apps, schema_editor):
    # Able to transfer
    group, created = Group.objects.get_or_create(name='transfer_user')
    if created:
        LOGGER.info('transfer_user Group created')

    # Archivist
    group, created = Group.objects.get_or_create(name='archivist_user')
    if created:
        LOGGER.info('archivist_user Group created')


class Migration(migrations.Migration):
    dependencies = [
        ('recordtransfer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
