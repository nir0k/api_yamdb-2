# Generated by Django 3.2 on 2023-04-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
