# Generated by Django 3.1 on 2020-08-18 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_ftuser_coalition_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=100)),
                ('secret', models.CharField(max_length=100)),
            ],
        ),
    ]
