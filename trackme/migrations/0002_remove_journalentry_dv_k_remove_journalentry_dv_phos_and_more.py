# Generated by Django 4.1.2 on 2022-11-30 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalentry',
            name='DV_k',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='DV_phos',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='DV_protein',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='DV_sodium',
        ),
        migrations.RemoveField(
            model_name='journalentry',
            name='DV_water',
        ),
    ]
