# Generated by Django 4.1.5 on 2023-01-29 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="host",
        ),
        migrations.RemoveField(
            model_name="room",
            name="topic",
        ),
    ]
