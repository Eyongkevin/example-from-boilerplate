# Generated by Django 5.0.6 on 2024-07-09 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0011_alter_authorsbooks_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="authorsbooks",
            options={
                "verbose_name": "Author and Book",
                "verbose_name_plural": "Authors and Books",
            },
        ),
    ]