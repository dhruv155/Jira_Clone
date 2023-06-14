# Generated by Django 4.1 on 2023-06-08 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("JiraApp", "0009_alter_issue_assignee_alter_issue_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="assignee",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="JiraApp.project"
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="sprint",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="JiraApp.sprint",
            ),
        ),
    ]
