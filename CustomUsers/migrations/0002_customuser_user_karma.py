# Generated by Django 2.2.6 on 2019-10-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUsers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_karma',
            field=models.IntegerField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
