# Generated by Django 2.2.6 on 2019-10-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUsers', '0006_remove_customuser_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='api_key',
            field=models.TextField(default='ej29jenfiwn9jndcjafiw'),
            preserve_default=False,
        ),
    ]