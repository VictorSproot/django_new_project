# Generated by Django 4.1.5 on 2023-01-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_authorbook_alter_bb_options_remove_bb_contacts_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authorbook',
            options={'ordering': ['title'], 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AddField(
            model_name='bb',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authorbook',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Адрес'),
        ),
    ]