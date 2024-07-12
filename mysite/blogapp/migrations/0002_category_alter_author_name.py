# Generated by Django 5.1a1 on 2024-07-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]