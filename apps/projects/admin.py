from django.contrib import admin
from .models import Project, Board, Card


class ProjectAdmin(admin.ModelAdmin):
    exclude = ['slug']
    readonly_fields = ['slug']


class BoardAdmin(admin.ModelAdmin):
    exclude = ['position']
    readonly_fields = ['position']


class CardAdmin(admin.ModelAdmin):
    exclude = ['slug', 'content']
    readonly_fields = ['slug', 'content']


admin.site.register(Card, CardAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Board, BoardAdmin)