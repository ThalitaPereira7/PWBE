# Generated by Django 5.1.6 on 2025-02-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
