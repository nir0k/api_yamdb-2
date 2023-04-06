# Generated by Django 3.2 on 2023-03-31 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0017_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(
                blank=True,
                choices=[(1, 'admin'), (2, 'user'), (3, 'moderator')],
                default=2,
                null=True,
            ),
        ),
    ]
