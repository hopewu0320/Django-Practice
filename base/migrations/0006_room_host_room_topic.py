# Generated by Django 4.1.5 on 2023-01-29 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0005_alter_room_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="host",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="room",
            name="topic",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="base.topic"
            ),
        ),
    ]
