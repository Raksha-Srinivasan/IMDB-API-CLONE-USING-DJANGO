# Generated by Django 4.0.2 on 2022-02-04 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0005_alter_watchlist_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='platform',
            new_name='platforms',
        ),
    ]
