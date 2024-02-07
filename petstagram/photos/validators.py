from django.core.exceptions import ValidationError


def validate_image_file_size_less_than_5mb(value):
    if value.size > 5242880:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')
