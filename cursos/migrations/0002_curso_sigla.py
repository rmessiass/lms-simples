# Generated by Django 2.0.6 on 2018-06-20 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='sigla',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]