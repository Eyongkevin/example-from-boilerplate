# Generated by Django 5.0.6 on 2024-06-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_alter_book_isbn_alter_book_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
