# Generated by Django 5.0.6 on 2024-06-26 14:25

import django.contrib.postgres.fields.ranges
import django.contrib.postgres.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myread", "0004_alter_statuspercent_percentage_read_range"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statuspercent",
            name="percentage_read_range",
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(
                blank=True,
                validators=[
                    django.contrib.postgres.validators.RangeMinValueValidator(0),
                    django.contrib.postgres.validators.RangeMaxValueValidator(101),
                ],
            ),
        ),
    ]
