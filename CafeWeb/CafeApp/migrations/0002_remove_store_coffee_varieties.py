# Generated by Django 5.1.5 on 2025-01-27 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CafeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='coffee_varieties',
        ),
    ]
