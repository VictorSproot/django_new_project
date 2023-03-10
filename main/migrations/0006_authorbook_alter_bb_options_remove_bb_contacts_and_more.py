# Generated by Django 4.1.5 on 2023-01-05 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_additionalimage_id_alter_advuser_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Автор')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc_for_find_cat', models.TextField(blank=True, db_index=True, verbose_name='Биография автора')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-created_at'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.RemoveField(
            model_name='bb',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='bb',
            name='price',
        ),
        migrations.AddField(
            model_name='bb',
            name='book_file',
            field=models.FileField(blank=True, null=True, upload_to=main.utilities.get_timestamp_path, verbose_name='Файл PDF'),
        ),
        migrations.AddField(
            model_name='bb',
            name='lang_category',
            field=models.IntegerField(choices=[(1, 'Русский'), (2, 'Английский')], db_index=True, default=1, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Добавил книгу'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subrubric', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='bb',
            name='author_book',
            field=models.ManyToManyField(to='main.authorbook', verbose_name='Автор'),
        ),
    ]
