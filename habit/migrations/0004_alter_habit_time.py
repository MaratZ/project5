# Generated by Django 5.1.3 on 2024-11-20 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0003_alter_habit_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.TimeField(
                blank=True,
                help_text="Установите время, когда необходимо выполнять привычку",
                null=True,
                verbose_name="Время",
            ),
        ),
    ]
