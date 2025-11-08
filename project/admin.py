from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_project',
        'project_address',
        'contact_person_name',
        'contact_person_number',
        'user',
        'created_by',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_by', 'created_at', 'updated_at')
    search_fields = ('name_of_project', 'contact_person_name', 'contact_person_number', 'project_address')
    ordering = ('-created_at',)

