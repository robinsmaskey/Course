# Generated by Django 4.0.6 on 2022-07-12 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_guardian_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='user',
        ),
        migrations.DeleteModel(
            name='Child',
        ),
        migrations.DeleteModel(
            name='Guardian',
        ),
    ]
