# Generated by Django 3.0.5 on 2020-05-09 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('location', models.CharField(max_length=100, verbose_name='Локация')),
                ('logo', models.ImageField(null=True, upload_to='company_logos', verbose_name='Логотип')),
                ('employee_count', models.IntegerField(null=True, verbose_name='Количество сотрудников')),
                ('description', models.TextField(verbose_name='Описание')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ['name'],
            },
        ),
    ]
