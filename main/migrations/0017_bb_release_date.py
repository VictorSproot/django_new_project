# Generated by Django 4.1.5 on 2023-02-08 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rubric_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='release_date',
            field=models.IntegerField(db_index=True, default=2000, verbose_name='Год выхода'),
            preserve_default=False,
        ),
    ]
