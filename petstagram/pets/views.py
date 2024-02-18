from django.urls import reverse, reverse_lazy

from django.views import generic as view

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
class PetCreateView(view.CreateView):
    # model = Pet  If have form we skip `model` and `fields`
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': 'Bobi',
            'pet_slug': self.object.slug,
        })


class PetDetailView(view.DetailView):
    # model = Pet  # or queryset
    queryset = Pet.objects.all().prefetch_related('petphoto_set') \
                .prefetch_related('petphoto_set__photolike_set') \
                .prefetch_related('petphoto_set__tagged_pets')
    template_name = 'pets/pet-details-page.html'
    # slug_field = 'slug'  - name of field in model
    slug_url_kwarg = 'pet_slug'  # name of param in `url`


class PetEditView(view.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'Bobi',

        return context

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': self.request.GET.get('username'),
            'pet_slug': self.object.slug
        })


class PetDeleteView(view.DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('index')

    extra_context = {
        'username': 'Bobi',
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = self.form_class(instance=self.object)
    #     context['form'] = form
    #
    #     return context


