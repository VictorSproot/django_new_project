# Generated by Django 4.1.5 on 2023-01-06 21:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_advuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, db_index=True, verbose_name='Описание'),
        ),
    ]