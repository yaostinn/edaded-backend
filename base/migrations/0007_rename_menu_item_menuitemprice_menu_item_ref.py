# Generated by Django 5.0 on 2024-01-30 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_menuitemprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitemprice',
            old_name='menu_item',
            new_name='menu_item_ref',
        ),
    ]
