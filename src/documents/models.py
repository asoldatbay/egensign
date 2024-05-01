from django.db import models

from src.templates.models import Template


class Document(models.Model):

    # mandatory
    url = models.CharField(max_length=255)

    # relations
    template = models.ForeignKey(
        to=Template,
        null=True,
        on_delete=models.SET_NULL,
    )
    # TODO: User relation

    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserData(models.Model):

    # mandatory
    filled_data = models.JSONField()

    # relations
    template = models.ForeignKey(
        to=Template,
        null=True,
        on_delete=models.SET_NULL,
    )
    document = models.ForeignKey(
        to=Document,
        on_delete=models.CASCADE,
        related_name='user_data',
    )

    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
