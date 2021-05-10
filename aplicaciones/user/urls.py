from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from aplicaciones.user.views import *


urlpatterns = [
    path(
        'beginning_user/',
        login_required(BeginningUser.as_view()),
        name='beginning_user'
    ),
    path(
        'list_user/',
        login_required(list_users),
        name='list_user'
    ),
    path(
        'new_user/',
        login_required(new_user),
        name='new_user'
    ),
    path(
        'delete_user/<int:id>',
        login_required(delete_user),
        name='delete_user'
    ),
    path(
        'update_user/<int:id>',
        login_required(update_user),
        name="update_user"
    ),
    path(
        'update_my_profile/',
        login_required(update_my_profile),
        name="update_user"
    ),
]
