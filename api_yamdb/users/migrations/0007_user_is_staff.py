# Generated by Django 3.2 on 2023-03-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0006_auto_20230330_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]