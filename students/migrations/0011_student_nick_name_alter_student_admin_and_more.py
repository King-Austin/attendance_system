# Generated by Django 4.2.7 on 2024-01-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_alter_student_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='nick_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='NickName'),
        ),
        migrations.AlterField(
            model_name='student',
            name='admin',
            field=models.CharField(default='False', max_length=10, verbose_name='Admin'),
        ),
        migrations.AlterField(
            model_name='student',
            name='auth_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Auth Code'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone'),
        ),
    ]
