# Generated by Django 4.1 on 2023-06-08 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("JiraApp", "0013_remove_issue_comment_comment_addedby_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="issue_id",
            new_name="issue",
        ),
    ]