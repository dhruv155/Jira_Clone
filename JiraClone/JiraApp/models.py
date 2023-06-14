from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import timedelta

# Create your models here.
HIGH = 'High'
LOW = 'Low'
MEDIUM = 'Medium'
STORY = 'Story'
SPILLOVER = 'Spillover'

LABEL_CHOICES = [
    (HIGH, 'High'),
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
    (STORY, 'Story'),
    (SPILLOVER, 'Spillover'),
]
STATUS = (
    ('open', 'open'),
    ('assigned', 'assigned'),
    ('in_progress', 'in_progress'),
    ('under_review', 'under_review'),
    ('done', 'done'),
    ('close', 'close')
)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    manager = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)

class Sprint(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        super().clean()
        if self.start_date and self.end_date:
            duration = self.end_date - self.start_date
            if duration != timedelta(days=6):
                raise ValidationError('Sprint duration should be exactly one week.')


class Comment(models.Model):
    description = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)



class Issue(models.Model):
    ISSUE_TYPE_CHOICES = (
        ('bug', 'Bug'),
        ('task', 'Task'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    issue_type = models.CharField(max_length=10, choices=ISSUE_TYPE_CHOICES)
    # assignee = models.CharField(max_length=50)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    labels = models.ManyToManyField('Label', choices=LABEL_CHOICES)
    status = models.CharField(max_length=150, choices=STATUS, default='open')
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, null=True, blank=True)
    comment= models.ForeignKey(Comment,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.title



class Label(models.Model):
    name = models.CharField(max_length=50, choices=LABEL_CHOICES)

