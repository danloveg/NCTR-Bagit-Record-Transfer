# Generated by Django 3.1.1 on 2020-11-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordtransfer', '0007_auto_20201105_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='attached_file',
            field=models.FileField(blank=True, null=True, upload_to='jobs/zipped_bags'),
        ),
    ]
