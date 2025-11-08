from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    # 🔹 Core Fields
    name_of_project = models.CharField(max_length=255)
    project_address = models.CharField(max_length=500)
    contact_person_name = models.CharField(max_length=255)
    contact_person_number = models.CharField(max_length=20)

    # 🔸 User Associations
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_projects',
        verbose_name='Assigned User'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_projects',
        verbose_name='Created By'
    )

    # 🕒 Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_project



