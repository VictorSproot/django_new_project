# Generated by Django 4.1.5 on 2023-01-05 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_authorbook_options_bb_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='Адрес'),
        ),
    ]
