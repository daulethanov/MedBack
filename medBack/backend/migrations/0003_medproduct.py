# Generated by Django 4.1.3 on 2022-12-04 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0002_blog_otvet"),
    ]

    operations = [
        migrations.CreateModel(
            name="MedProduct",
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
            ],
        ),
    ]