# Generated by Django 2.2.5 on 2020-01-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('populate_data', '0003_auto_20200118_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]