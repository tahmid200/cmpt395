# Generated by Django 2.0 on 2018-03-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20180318_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentcreation',
            name='curent_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parentcreation',
            name='monthly_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parentcreation',
            name='total_hours',
            field=models.IntegerField(default=0),
        ),
    ]
