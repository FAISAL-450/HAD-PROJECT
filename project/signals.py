from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Project
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Project)
def handle_project_save(sender, instance, created, **kwargs):
    project_name = instance.name_of_project
    created_by = getattr(instance.created_by, 'username', 'Unknown')

    if created:
        logger.info(f"New project created: {project_name} by {created_by}")
    else:
        logger.info(f"Project updated: {project_name}")

@receiver(post_delete, sender=Project)
def handle_project_delete(sender, instance, **kwargs):
    project_name = instance.name_of_project
    logger.info(f"Project deleted: {project_name}")

