from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_dni = models.ForeignKey(Tiposdni, on_delete=models.PROTECT, null=False)
    dni = models.IntegerField()
    nombres = models.CharField(max_length=200)
    tel = models.IntegerField()
    correo = models.CharField(max_length=300)
    url_selfi = models.CharField(max_length=5000)
    url_documento = models.CharField(max_length=5000)
    resultado_fac = models.CharField(max_length=20)
    fecha = models.DateField()

    def __str__(self):
        return self.nombres

class Tiposdni(models.Model):
    id = models.AutoField(primary_key=True)
    tipodni = models.CharField(max_length=100)

    def __str__(self):
        return self.tipodni

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






