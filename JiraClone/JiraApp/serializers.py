from rest_framework import serializers
from JiraApp.models import Project, Issue,Label,Sprint,Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    user= UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    # project = ProjectSerializer(read_only=True,many=True)
    project = ProjectSerializer(read_only=True)
    assignee = UserSerializer(read_only=True)
    comment = CommentSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']


class IssueOfUserSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True)
    class Meta:
        model = Issue
        fields = '__all__'

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'




