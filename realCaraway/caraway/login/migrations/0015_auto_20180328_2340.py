# Generated by Django 2.0.2 on 2018-03-28 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20180320_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parentcreation',
            old_name='curent_hours',
            new_name='current_hours',
        ),
    ]
