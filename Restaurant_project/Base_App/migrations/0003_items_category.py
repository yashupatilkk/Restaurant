# Generated by Django 5.1.7 on 2025-03-31 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0002_itemlist_delete_yourmodel_remove_aboutus_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Base_App.itemlist'),
        ),
    ]
