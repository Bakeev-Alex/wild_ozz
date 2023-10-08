# Generated by Django 4.2.5 on 2023-09-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog2",
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
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
            ],
            options={
                "verbose_name": "Блог_2",
                "verbose_name_plural": "Блоги_2",
                "db_table": "blog_blog_2",
            },
        ),
    ]
