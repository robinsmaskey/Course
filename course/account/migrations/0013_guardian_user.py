# Generated by Django 4.0.6 on 2022-07-12 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_guardian_user_guardian_name_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardian',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
