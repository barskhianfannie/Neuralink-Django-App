# Generated by Django 4.0.3 on 2022-04-13 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='device',
        ),
    ]
