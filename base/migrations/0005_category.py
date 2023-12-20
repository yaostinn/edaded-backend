# Generated by Django 5.0 on 2023-12-20 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_isvisible_restaurant_is_visible_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.base')),
                ('name', models.CharField(max_length=255)),
                ('restaurant_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.restaurant')),
            ],
            bases=('base.base',),
        ),
    ]
