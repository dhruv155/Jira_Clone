from django.contrib import admin

# Register your models he
from JiraApp.models import Issue, Project,Label,Sprint

#admin.site.register(Issue)


# admin.site.register(Project)

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'manager']

@admin.register(Issue)
class IssueModelAdmin(admin.ModelAdmin):
    list_display = ['id','project', 'title', 'description','assignee','issue_type']

@admin.register(Label)
class LAbelModelAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Sprint)
class SprintModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','start_date','end_date']
