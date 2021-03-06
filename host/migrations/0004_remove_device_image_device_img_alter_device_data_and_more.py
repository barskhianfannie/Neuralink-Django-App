# Generated by Django 4.0.3 on 2022-04-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0003_device_data_alter_device_dateexpires_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='image',
        ),
        migrations.AddField(
            model_name='device',
            name='img',
            field=models.FileField(blank=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='device',
            name='data',
            field=models.TextField(max_length=500000, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='dateExpires',
            field=models.DateTimeField(default=None, null=True, verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='device',
            name='dateManufactured',
            field=models.DateTimeField(default=None, null=True, verbose_name='Manufactured Date'),
        ),
        migrations.AlterField(
            model_name='device',
            name='slug',
            field=models.SlugField(blank=True, default='device26178', max_length=250),
        ),
    ]
