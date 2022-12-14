# Generated by Django 4.0.6 on 2022-07-27 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'страна',
                'verbose_name_plural': 'страны',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=2, verbose_name='Код страны')),
            ],
            options={
                'verbose_name': 'страна',
                'verbose_name_plural': 'страны',
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'город',
                'verbose_name_plural': 'города',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=10, verbose_name='Код региона')),
            ],
            options={
                'verbose_name': 'регион',
                'verbose_name_plural': 'регионы',
            },
        ),
        migrations.AddField(
            model_name='airport',
            name='coordinates',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='airport',
            name='elevation_ft',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='airport',
            name='gps_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='airport',
            name='iata_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.airporttype', verbose_name='Тип аэропорта'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')),
                ('comment', models.CharField(max_length=255, verbose_name='Наименование')),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='avia.airport', verbose_name='аэропорт')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'коментарии',
            },
        ),
        migrations.AddField(
            model_name='airport',
            name='continent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.continent', verbose_name='Континент'),
        ),
        migrations.AddField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.country', verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='airport',
            name='municipality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.municipality', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='airport',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.region', verbose_name='Регион'),
        ),
    ]
