# Generated by Django 2.2.6 on 2019-10-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUsers', '0002_customuser_user_karma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_karma',
            field=models.IntegerField(),
        ),
    ]