# Generated by Django 4.0.6 on 2022-07-12 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_guardian_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]