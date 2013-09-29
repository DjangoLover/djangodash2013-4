from django.contrib import admin
from .models import Project, Board


class ProjectAdmin(admin.ModelAdmin):
    exclude = ['slug']
    readonly_fields = ['slug']


class BoardAdmin(admin.ModelAdmin):
    exclude = ['position']
    readonly_fields = ['position']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Board, BoardAdmin)