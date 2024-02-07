from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_image_file_size_less_than_5mb


# Create your models here.
class PetPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        blank=False,
        null=False,
        validators=(
            validate_image_file_size_less_than_5mb,
        ),
    )
    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )
    tagged_pets = models.ManyToManyField(
        to=Pet,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    modified_at = models.DateTimeField(
        auto_now=True,
    )
