# Generated by Django 4.2.7 on 2024-02-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0004_alter_course_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="day_number",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
