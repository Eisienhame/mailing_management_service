# Generated by Django 4.2.3 on 2023-07-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='mailings',
        ),
        migrations.AddField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(blank=True, null=True, to='main.client', verbose_name='клиенты'),
        ),
    ]
