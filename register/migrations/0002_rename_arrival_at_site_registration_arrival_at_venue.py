# Generated by Django 4.2.7 on 2023-11-24 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='arrival_at_site',
            new_name='arrival_at_venue',
        ),
    ]
