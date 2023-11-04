from django.db import models

class mUsuario(models.Model):

    CvUser = models.CharField(max_length=20, unique=True, primary_key=True)
    CvPerson = models.CharField(max_length=20)
    Login = models.CharField(max_length=30, unique=True)
    Password = models.CharField(max_length=128) 
    FecIni = models.DateField()
    FecFin = models.DateField()
    EdoCta = models.BooleanField(default=False)
