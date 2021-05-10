from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, password=None, is_admin=False):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            is_admin=is_admin
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(
            self,
            username,
            email,
            name,
            password=None):
        return self._create_user(
            username,
            email,
            name,
            password)

    def create_superuser(
            self,
            username,
            email,
            name,
            password=None):
        return self._create_user(
            username,
            email,
            name,
            password,
            True
        )


class User(AbstractBaseUser):
    username = models.CharField(
        'Nombre de user',
        unique=True,
        max_length=100
    )

    email = models.EmailField(
        'Correo Electrónico',
        max_length=254,
        unique=True
    )

    name = models.CharField(
        'Nombres',
        max_length=200,
        blank=True,
        null=True
    )

    lastname = models.CharField(
        'Apellidos',
        max_length=200,
        blank=True,
        null=True
    )

    image = models.ImageField(
        'Imagen de Perfil',
        upload_to='perfil/',
        max_length=200,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_admin = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return f'{self.name},{self.lastname}'

    def has_perm(self, perm, ob=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
