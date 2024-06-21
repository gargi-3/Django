# Generated by Django 5.0.6 on 2024-06-06 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid',
            new_name='completed',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]
