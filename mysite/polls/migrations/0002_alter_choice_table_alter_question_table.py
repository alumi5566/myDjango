# Generated by Django 4.2.7 on 2023-12-01 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='choice',
            table='default',
        ),
        migrations.AlterModelTable(
            name='question',
            table='default',
        ),
    ]
