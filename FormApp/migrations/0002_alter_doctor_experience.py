# Generated by Django 4.2.7 on 2024-03-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FormApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="experience",
            field=models.IntegerField(),
        ),
    ]
