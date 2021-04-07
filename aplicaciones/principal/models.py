from django.db import models

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
    url_selfi = models.ImageField(upload_to='images/')
    url_documento = models.CharField(max_length=5000)
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






