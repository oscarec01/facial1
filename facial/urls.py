from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from django.contrib.auth.decorators import login_required
from aplicaciones.principal.views import *
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(inicio), name='index'),
    path('user/', include(('aplicaciones.user.urls', 'user'))),
    path('crear_persona/', login_required(crearPersona),name='crear_persona'),
    path('consulta/', login_required(consulta),name='consulta'),
    path('ver_caso/<int:id>', login_required(ver_caso)),
    path('valida_caso/<int:id>', login_required(valida_caso)),
    path('prueba', prueba),
    path("accounts/login/", LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name="logout")
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


