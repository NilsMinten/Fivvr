# Generated by Django 2.2.6 on 2019-10-25 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Services', '0005_auto_20191025_1111'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='processing', max_length=15)),
                ('userFeedback', models.CharField(default=django.db.models.deletion.SET_NULL, max_length=15)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.Service')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_user', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
