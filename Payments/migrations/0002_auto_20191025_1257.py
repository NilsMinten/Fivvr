# Generated by Django 2.2.6 on 2019-10-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='userFeedback',
            field=models.CharField(default='', max_length=15),
        ),
    ]
