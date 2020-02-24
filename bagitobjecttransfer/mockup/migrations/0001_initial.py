# Generated by Django 3.0.3 on 2020-02-24 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bagging_date', models.DateTimeField(verbose_name='date bagged')),
                ('bag_location', models.CharField(max_length=256)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mockup.User')),
            ],
        ),
    ]
