from django.urls import path, include

from petstagram.accounts.views import \
    singup_profile, signin_profile, singout_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('register/', singup_profile, name='signup profile'),
    path('login/', signin_profile, name='signin profile'),
    path('logout/', singout_profile, name='signout profile'),
    path('profile/<int:pk>/', include([
        path('', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
