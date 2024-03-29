# Generated by Django 3.2 on 2023-03-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0014_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(
                choices=[(1, 'admin'), (2, 'user'), (3, 'moderator')],
                default=2,
            ),
        ),
    ]
