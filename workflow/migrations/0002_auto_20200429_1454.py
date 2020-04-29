# Generated by Django 3.0.5 on 2020-04-29 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'ordering': ['title'], 'verbose_name': 'Специальность', 'verbose_name_plural': 'Специальности'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['title'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='slug',
        ),
    ]
