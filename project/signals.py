from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Project
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Project)
def handle_project_save(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New project created: {instance.name_of_project} by {instance.created_by.username}")
    else:
        logger.info(f"Project updated: {instance.name_of_project}")

@receiver(post_delete, sender=Project)
def handle_project_delete(sender, instance, **kwargs):
    logger.info(f"Project deleted: {instance.name_of_project}")
