# Generated by Django 5.0.6 on 2024-07-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0003_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
