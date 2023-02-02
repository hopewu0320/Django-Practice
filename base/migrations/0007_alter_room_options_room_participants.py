# Generated by Django 4.1.5 on 2023-02-02 06:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0006_room_host_room_topic"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ("-created", "-updated")},
        ),
        migrations.AddField(
            model_name="room",
            name="participants",
            field=models.ManyToManyField(
                blank=True, related_name="participants", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
