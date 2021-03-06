# Generated by Django 4.0.2 on 2022-04-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=50, verbose_name='Название')),
                ('about1', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Названия')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Clothers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=50, verbose_name='Название')),
                ('description1', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_name', models.CharField(max_length=80, verbose_name='Название')),
                ('about2', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, verbose_name='Название')),
                ('description2', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Username')),
                ('is_published', models.BooleanField(default=True, verbose_name='I read regulations')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Username')),
                ('name', models.CharField(max_length=255, verbose_name='First name')),
                ('surname', models.CharField(max_length=255, verbose_name='Last name')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('repeat', models.CharField(max_length=255, verbose_name='Repeat password')),
                ('requement', models.CharField(max_length=255, verbose_name='phone')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Singers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50, verbose_name='Название')),
                ('about', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
    ]
