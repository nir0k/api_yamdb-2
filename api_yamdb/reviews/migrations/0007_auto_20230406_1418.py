# Generated by Django 3.2 on 2023-04-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('reviews', '0006_alter_genre_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={
                'ordering': ['pub_date'],
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(
                fields=('title', 'author'), name='unique_review'
            ),
        ),
    ]
