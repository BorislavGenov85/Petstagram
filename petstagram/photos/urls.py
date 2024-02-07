from django.urls import path, include

from petstagram.photos.views import create_photo, edit_photo, details_photo

urlpatterns = (
    path('add/', create_photo, name='create photo'),
    path('<int:pk>/', include([
        path('', details_photo, name='details photo'),
        path('edit/', edit_photo, name='edit photo'),
    ])),
)