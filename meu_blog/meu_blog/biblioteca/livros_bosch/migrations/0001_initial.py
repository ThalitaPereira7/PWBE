# Generated by Django 5.1.7 on 2025-03-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.TextField()),
                ('ano', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Livros',
            },
        ),
    ]
