# Generated by Django 2.2.5 on 2020-01-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='txn_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
    ]