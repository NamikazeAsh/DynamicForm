# Generated by Django 4.2.7 on 2024-03-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FormApp", "0005_alter_doctor_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="experience",
            field=models.CharField(max_length=100),
        ),
    ]