# Generated by Django 5.0 on 2023-12-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, null=True, verbose_name='Анонс')),
                ('full_text', models.TextField(null=True, verbose_name='Статья')),
                ('Date', models.DateTimeField(null=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
