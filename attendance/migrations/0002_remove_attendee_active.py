# Generated by Django 4.2.7 on 2024-02-03 11:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attendee",
            name="active",
        ),
    ]
