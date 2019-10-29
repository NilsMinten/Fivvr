# Generated by Django 2.2.6 on 2019-10-15 12:16

import datetime
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
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=140)),
                ('service_description', models.TextField(max_length=10000)),
                ('service_created', models.DateTimeField(default=datetime.datetime(2019, 10, 15, 12, 16, 51, 351400))),
                ('service_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
