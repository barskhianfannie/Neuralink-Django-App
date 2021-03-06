# Generated by Django 4.0.3 on 2022-04-12 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceName', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, upload_to='static/')),
                ('dateManufactured', models.DateTimeField(verbose_name='date published')),
                ('dateExpires', models.DateTimeField(verbose_name='end date')),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
