# Generated by Django 3.1.5 on 2021-01-29 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Under_Caregories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название под категории')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='under_category', to='generator.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Под категория',
                'verbose_name_plural': 'Под категории',
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название сайта')),
                ('url', models.URLField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('under_caregory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to='generator.under_caregories', verbose_name='Под категория')),
            ],
            options={
                'verbose_name': 'Сайт',
                'verbose_name_plural': 'Сайты',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('url', models.URLField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='generator.sites', verbose_name='Сайт')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]