# Generated by Django 5.0.6 on 2024-06-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myread", "0002_statuspercent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statuspercent",
            name="read_status",
            field=models.CharField(max_length=10),
        ),
    ]
