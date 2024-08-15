# Generated by Django 5.0.6 on 2024-07-02 11:12

import datetime
import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reader", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NIC",
            fields=[
                (
                    "id_number",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("delivery_date", models.DateField()),
                (
                    "expiration_date",
                    models.DateField(
                        default=django.db.models.expressions.CombinedExpression(
                            models.F("delivery_date"),
                            "+",
                            models.Value(datetime.timedelta(days=1826, seconds=21600)),
                        )
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="nic",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "delivery_date__gte",
                        django.db.models.expressions.CombinedExpression(
                            models.F("expiration_date"),
                            "-",
                            models.Value(datetime.timedelta(days=1826, seconds=21600)),
                        ),
                    )
                ),
                name="reader_nic_date_check",
            ),
        ),
    ]