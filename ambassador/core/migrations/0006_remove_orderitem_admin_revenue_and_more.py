# Generated by Django 5.0.7 on 2024-08-11 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='admin_revenue',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='ambassador_revenue',
        ),
    ]
