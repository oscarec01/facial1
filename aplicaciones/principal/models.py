from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Tiposdni(models.Model):
    id = models.AutoField(primary_key=True)
    tipodni = models.CharField(max_length=100)

    def __str__(self):
        return self.tipodni


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_dni = models.ForeignKey(Tiposdni, on_delete=models.PROTECT, null=False)
    dni = models.IntegerField()
    nombres = models.CharField(max_length=200)
    tel = models.BigIntegerField()
    correo = models.CharField(max_length=300)
    url_selfi = models.ImageField(upload_to='images/selfie/', default='images/selfie/no-images.jpg')
    url_documento = models.ImageField(upload_to='images/doc/', default='images/doc/no-images.jpg')
    resultado_fac = models.CharField(max_length=20)
    fecha = models.DateField(null=False, blank=False, auto_now=True)

    def __str__(self):
        return self.nombres


class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado


class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_dni = models.ForeignKey(Tiposdni, on_delete=models.PROTECT, null=False)
    dni = models.IntegerField()
    nombres = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    contrasenia = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=False, default=1)

    def __str__(self):
        return self.nombres


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, name, lastname, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email!!!')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            lastname=lastname
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, username, name, lastname, password):
        usuario = self.create_user(
            email,
            username=username,
            name=name,
            lastname=lastname,
            password=password
        )
        usuario.user_admin = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    username = models.CharField("Username", unique=True, max_length=100)
    email = models.CharField("Email", unique=True, max_length=255)
    name = models.CharField("Name", blank=True, max_length=100, null=True)
    lastname = models.CharField("Lastname", blank=True, max_length=100, null=True)
    image = models.ImageField("Image", upload_to='perfil/', height_field=None, width_field=None, max_length=200, blank=True, null=True)
    user_active = models.BooleanField(default=True)
    user_admin = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'lastname']

    def __str__(self):
        return f'Usuario {self.username}, {self.lastname}'

    def has_perm(self):
        return True

    def has_module_perms(self):
        return True

    @property
    def is_staff(self):
        return self.user_admin






