from django.db import models

class mPersona(models.Model):
    CvPersona = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    ApePat = models.CharField(max_length=20)
    ApeMat = models.CharField(max_length=20)
    Direccion = models.TextField(max_length=100, null=True, blank=True)
    Telefono = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M')
    Trabajo = models.CharField(max_length=100, null=True, blank=True)
    FecNac = models.DateTimeField(null=True, blank=True)
    TpPerson = models.CharField(max_length=1, choices=[('N', 'Natural'), ('J', 'Jurídica')], default='N')

    def __str__(self):
        return self.Nombre