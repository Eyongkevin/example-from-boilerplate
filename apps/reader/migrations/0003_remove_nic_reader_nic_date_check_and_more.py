# Generated by Django 5.0.6 on 2024-07-02 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reader", "0002_nic_nic_reader_nic_date_check"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="nic",
            name="reader_nic_date_check",
        ),
        migrations.RemoveField(
            model_name="nic",
            name="expiration_date",
        ),
    ]