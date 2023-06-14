from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Issue, Label,Sprint,Comment
from .serializers import ProjectSerializer, IssueSerializer, IssueOfUserSerializer, LabelSerializer,SprintSerializer,CommentSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ProjectAPIView(APIView):

    # Create your views here.
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IssueAPIView(APIView):
    def post(self, request):
        project_id = request.data.project_id
        print("LINE 53")
        print(project_id)
        if not project_id:
            return Response({'error': 'project_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = IssueSerializer(data)
        if serializer.is_valid():
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)


class IssueAPIDetailView(APIView):
    def get(self, request, project_id):
        issues = Issue.objects.filter(project_id=project_id)
        # issues = issues.objects.filter(project_id=project_id)
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)


class AssignIssueAPIView(APIView):
    def put(self, request, issue_id, user_id):
        try:
            issue = Issue.objects.get(id=issue_id)
            user = User.objects.get(id=user_id)
            issue.assigned_to = user
            issue.save()
            serializer = IssueSerializer(issue)
            return Response(serializer.data)
        except Issue.DoesNotExist:
            return Response(status=404)
        except User.DoesNotExist:
            return Response(status=404)


class AssignedIssuesAPIView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            issues = Issue.objects.filter(assignee=user)
            serializer = IssueOfUserSerializer(issues, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=404)


class AddLabelToIssueAPIView(APIView):

    def put(self, request, issue_id, label_id):
        try:
            issue = Issue.objects.get(id=issue_id)
            label = Label.objects.get(id=label_id)
            issue.labels.add(label)
            issue.save()
            serializer = IssueSerializer(issue)

            return Response(serializer.data)
        except Issue.DoesNotExist:
            return Response({"message": "issue does not exist"}, status=404)
        except Label.DoesNotExist:
            return Response({"message": "Label does not exist"}, status=404)


class LabelAPI(APIView):
    def get(self, request):
        labels = Label.objects.all()
        if labels is None:
            return Response({"mesaage": "no labels "})
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)


class UpdateIssueStatusAPIView(APIView):
    def put(self, request):

        issue_id = request.data.get('issue_id')
        updated_status = request.data.get('updated_status')
        STATUS = [
            'open',
            'assigned',
            'in_progress',
            'under_review',
            'done',
            'close'
        ]
        try:
            issue = Issue.objects.get(id=issue_id)
            print(issue.status)

            i = 1;
            while i < 6:
                prev = STATUS[i - 1]
                curr = STATUS[i]
                if updated_status == curr and prev == issue.status:
                    issue.status = updated_status

                    break
                else:
                    i = i + 1
            issue.save()
            if i == 6:
                return Response({'message': 'can not update'})
            else:
                return Response({'message': 'Issue status updated successfully.'})

        except Issue.DoesNotExist:
            return Response({'message': 'Issue not found.'}, status=404)


# Sprint API view
class SprintAPIView(APIView):

    # Create your views here.
    def get(self, request):
        sprints = Sprint.objects.all()
        serializer = SprintSerializer(sprints, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Retrieve and validate the request data
        name = request.data.get('name')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        try:
            sprint = Sprint(name=name, start_date=start_date, end_date=end_date)
            sprint.full_clean()  # Perform model validation
            sprint.save()
            return Response({'message': 'Sprint created successfully.'})
        except ValidationError as e:
            return Response({'message': str(e)}, status=400)

    def put(self, request, issue_id, sprint_id):
        try:
            issue = Issue.objects.get(id=issue_id)
            sprint = Sprint.objects.get(id=sprint_id)
            issue.sprint = sprint
            issue.save()
            return Response({'message': 'Sprint set for the issue successfully.'})
        except Issue.DoesNotExist:
            return Response({'message': 'Issue not found.'}, status=404)
        except Sprint.DoesNotExist:
            return Response({'message': 'Sprint not found.'}, status=404)

class MoveIssuesAPIView(APIView):
    def post(self, request):
        issues = request.data.get('issues')
        source_sprint_id = request.data.get('source_sprint')
        target_sprint_id = request.data.get('target_sprint')

        try:
            source_sprint = Sprint.objects.get(id=source_sprint_id)
            target_sprint = Sprint.objects.get(id=target_sprint_id)
        except Sprint.DoesNotExist:
            return Response({'message': 'Invalid sprint ID provided.'}, status=400)

        try:
            for issue_id in issues:
                issue = Issue.objects.get(id=issue_id, sprint=source_sprint)
                issue.sprint = target_sprint
                issue.save()
            return Response({'message': 'Issues moved successfully.'})
        except Issue.DoesNotExist:
            return Response({'message': 'Invalid issue ID provided.'}, status=400)

class AddCommentAPIView(APIView):
    def post(self, request):
        try:
            issue = Issue.objects.get(id=request.data.get('issue_id'))
            user = User.objects.get(id=request.data.get('user_id'))
            print(request.data)
            description = "abcd"
            addedBy=user
            comment = Comment.objects.create(issue=issue, description=description)

            comment.save()
            return Response({'message': 'comment set for the issue successfully.'})
        except Issue.DoesNotExist:
            return Response({'message': 'Issue not found.'}, status=404)
        except User.DoesNotExist:
            return Response({'message': 'User not found.'}, status=404)

    def put(self, request):
        try:
            issue = Issue.objects.get(id=request.data.get('issue_id'))
            user = User.objects.get(id=request.data.get('user_id'))
            #comment=Comment(description=request.data.get('description'))
            description = request.data.get('description')
            comment = Comment.objects.create(issue=issue, description=description,user=user)
            issue.comment=comment
            issue.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=201)
            #return Response({'message': 'Comment set for the issue successfully.'})
        except Issue.DoesNotExist:
            return Response({'message': 'Issue not found.'}, status=404)
        except Sprint.DoesNotExist:
            return Response({'message': 'Sprint not found.'}, status=404)