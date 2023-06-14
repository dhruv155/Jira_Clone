# Generated by Django 4.1 on 2023-06-07 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("body", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("manager", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Issue",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "issue_type",
                    models.CharField(
                        choices=[("bug", "Bug"), ("task", "Task")], max_length=10
                    ),
                ),
                ("assignee", models.CharField(max_length=50)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="JiraApp.project",
                    ),
                ),
            ],
        ),
    ]
