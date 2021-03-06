# Generated by Django 2.2.13 on 2020-06-26 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubmember',
            name='introducing',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='자기소개'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clubmember',
            name='is_join',
            field=models.BooleanField(default=False, verbose_name='가입여부'),
        ),
    ]
