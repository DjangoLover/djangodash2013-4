from django.contrib import admin
from .models import Project, Board, Card, ProjectComment, CardComment


class ProjectAdmin(admin.ModelAdmin):
    exclude = ['slug']
    readonly_fields = ['slug']


class BoardAdmin(admin.ModelAdmin):
    exclude = ['position']
    readonly_fields = ['position']


class CardAdmin(admin.ModelAdmin):
    exclude = ['slug', 'content']
    readonly_fields = ['slug', 'content']


class ProjectCommentAdmin(admin.ModelAdmin):
    exclude = ['content']
    readonly_fields = ['content']


class CardCommentAdmin(admin.ModelAdmin):
    exclude = ['content']
    readonly_fields = ['content']


admin.site.register(CardComment, CardCommentAdmin)
admin.site.register(ProjectComment, ProjectCommentAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Board, BoardAdmin)