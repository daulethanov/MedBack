# Generated by Django 4.1.3 on 2022-12-04 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("question", models.TextField(verbose_name="Вопрос")),
            ],
        ),
        migrations.CreateModel(
            name="Otvet",
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
                (
                    "otvet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.blog"
                    ),
                ),
            ],
        ),
    ]
