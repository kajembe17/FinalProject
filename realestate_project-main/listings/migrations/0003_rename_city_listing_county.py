# Generated by Django 4.0.2 on 2022-02-24 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_remove_listing_state_listing_suburb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='city',
            new_name='county',
        ),
    ]