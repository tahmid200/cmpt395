# Generated by Django 2.0 on 2018-03-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_delete_classcreation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentcreation',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
