# Generated by Django 4.1.3 on 2022-11-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('build', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(choices=[('BENZINE', 'Benzine'), ('DIESEL', 'Diesel')], default='BENZINE', max_length=8)),
            ],
            options={
                'db_table': 'autos',
            },
        ),
        migrations.CreateModel(
            name='Fabrikant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
    ]
