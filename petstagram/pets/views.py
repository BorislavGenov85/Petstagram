from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
def create_pet(request):
    pet_form = PetCreateForm(request.POST or None)

    if request.method == 'POST':
        if pet_form.is_valid():
            created_pet = pet_form.save()
            return redirect(details_pet, username='Bobi', pet_slug=created_pet.slug)

    context = {
        'pet_form': pet_form,
    }
    return render(request, 'pets/pet-add-page.html', context)


def details_pet(request, username, pet_slug):
    context = {
        'pet': Pet.objects.get(slug=pet_slug)
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    pet_form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if pet_form.is_valid():
            pet_form.save()
            return redirect('details_pet', username=username, pet_slug=pet_slug)

    context = {
        'pet_form': pet_form,
        'username': username,
        'pet': pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    pet_form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        pet_form.save()
        return redirect('index')

    context = {
        'pet_form': pet_form,
        'username': username,
        'pet': pet
    }
    return render(request, 'pets/pet-delete-page.html', context)
