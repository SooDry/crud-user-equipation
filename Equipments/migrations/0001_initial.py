# Generated by Django 4.1 on 2022-08-22 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('code', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
            ],
        ),
    ]
