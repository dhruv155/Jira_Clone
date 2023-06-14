"""
URL configuration for JiraClone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from JiraApp.views import ProjectAPIView,ProjectDetailAPI,IssueAPIView,IssueAPIDetailView,AssignIssueAPIView,AssignedIssuesAPIView,AddLabelToIssueAPIView,LabelAPI,UpdateIssueStatusAPIView,SprintAPIView,MoveIssuesAPIView,AddCommentAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', ProjectAPIView.as_view()),
    path('projects/<int:pk>/', ProjectDetailAPI.as_view()),
    path('issue/',IssueAPIView.as_view()),
    path('issue/<int:project_id>/',IssueAPIDetailView.as_view()),
    path('issue/<int:issue_id>/assign/<int:user_id>/', AssignIssueAPIView.as_view()),
    path('users/<int:user_id>/issues/', AssignedIssuesAPIView.as_view()),
    path('issue/<int:issue_id>/add_label/<int:label_id>/', AddLabelToIssueAPIView.as_view()),
    path('label/getall', LabelAPI.as_view()),
    path('issue/update_status/', UpdateIssueStatusAPIView.as_view()),
    path('sprint/',SprintAPIView.as_view()),
    path('api/issues/<int:issue_id>/set-sprint/<int:sprint_id>/', SprintAPIView.as_view()),

    path('api/move-issues/', MoveIssuesAPIView.as_view(), name='move-issues-api'),
    path('issue/add-comment/',AddCommentAPIView.as_view())


]
