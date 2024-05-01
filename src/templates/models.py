import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Template(models.Model):

    # Informative
    name = models.CharField(max_length=255)
    description = models.TextField()

    # Mandatory
    url = models.CharField(max_length=255)
    doc_fields = models.JSONField()
    script_code = models.CharField(max_length=255, blank=True, null=True)

    # Date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(pre_save, sender=Template)
def generate_script_code(sender, instance, **kwargs):
    if not instance.script_code:  # Check if script_code is blank
        instance.script_code = str(uuid.uuid4())  # Generate random UUID
