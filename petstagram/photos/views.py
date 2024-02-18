from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import PetPhoto


# Create your views here.
class PetPhotoCreateView(views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    if __name__ == '__main__':
        queryset = PetPhoto.objects.all() \
            .prefetch_related('petphoto_set__tagged_pets')

    def get_success_url(self):
        return reverse('details photo', kwargs={
            'pk': self.object.pk,
        })


class PetPhotoDetailView(views.DetailView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related('tagged_pets') \
        .prefetch_related('photolike_set') \
        .prefetch_related('photocomment_set')
    template_name = 'photos/photo-details-page.html'


class PetPhotoEditView(views.UpdateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related('tagged_pets')
    template_name = 'photos/photo-edit-page.html'
    form_class = PetPhotoEditForm

    def get_success_url(self):
        return reverse_lazy('details photo', kwargs={
           'pk': self.object.pk,
        })
