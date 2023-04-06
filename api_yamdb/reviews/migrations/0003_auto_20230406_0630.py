# Generated by Django 3.2 on 2023-04-06 06:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('reviews', '0002_auto_20230405_1824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={
                'ordering': ['-pub_date'],
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='pub_date',
        ),
    ]