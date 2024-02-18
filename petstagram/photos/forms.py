from django import forms

from petstagram.core.form_mixins import ReadOnlyFieldsFormMixin
from petstagram.photos.models import PetPhoto


class PetPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'location', 'tagged_pets')


class PetPhotoCreateForm(PetPhotoBaseForm):
    pass


class PetPhotoEditForm(ReadOnlyFieldsFormMixin, PetPhotoBaseForm):
    readonly_fields = ('photo', 'tagged_pets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()
