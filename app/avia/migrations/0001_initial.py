# Generated by Django 4.0.6 on 2022-07-27 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Вид аэропорта',
                'verbose_name_plural': 'Виды аэропортов',
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.CharField(max_length=10, unique=True, verbose_name='Идентификатор')),
                ('local_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.airporttype', verbose_name='Тип аэропорта')),
            ],
            options={
                'verbose_name': 'аэропорт',
                'verbose_name_plural': 'аэропорты',
            },
        ),
    ]
