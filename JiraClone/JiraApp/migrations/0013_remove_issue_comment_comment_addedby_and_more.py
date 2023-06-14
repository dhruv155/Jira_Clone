# Generated by Django 4.1 on 2023-06-08 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("JiraApp", "0012_rename_body_comment_comment_issue_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="issue",
            name="comment",
        ),
        migrations.AddField(
            model_name="comment",
            name="addedBy",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="issue_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="JiraApp.issue",
            ),
        ),
    ]