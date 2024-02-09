from django.db import models

from petstagram.photos.models import PetPhoto


# Create your models here.
class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    modified_at = models.DateTimeField(
        auto_now=True,
    )
    pet_photo = models.ForeignKey(
        to=PetPhoto,
        on_delete=models.RESTRICT,
    )


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(
        to=PetPhoto,
        on_delete=models.RESTRICT,
    )

