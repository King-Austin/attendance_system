# Generated by Django 4.2.7 on 2024-02-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0002_remove_attendee_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendee",
            name="signed_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]