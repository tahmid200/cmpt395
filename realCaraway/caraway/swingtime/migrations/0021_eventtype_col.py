# Generated by Django 2.0.2 on 2018-04-09 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swingtime', '0020_auto_20180409_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='col',
            field=models.IntegerField(default=0),
        ),
    ]
