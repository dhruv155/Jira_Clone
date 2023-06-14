# Generated by Django 4.1 on 2023-06-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("JiraApp", "0002_alter_issue_assignee"),
    ]

    operations = [
        migrations.CreateModel(
            name="Label",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="issue",
            name="labels",
            field=models.ManyToManyField(
                choices=[
                    ("High", "High"),
                    ("Low", "Low"),
                    ("Medium", "Medium"),
                    ("Story", "Story"),
                    ("Spillover", "Spillover"),
                ],
                to="JiraApp.label",
            ),
        ),
    ]