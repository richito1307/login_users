from django.db import models

class cNombre(models.Model):
    CvNombre = models.AutoField(primary_key=True)
    DsNombre = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.DsNombre

class cApePat(models.Model):
    CvApePat = models.AutoField(primary_key=True)
    DsApePat = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.DsApePat

class cApeMat(models.Model):
    CvApeMat = models.AutoField(primary_key=True)
    DsApeMat = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.DsApeMat

class cAficion(models.Model):
    CvAficion = models.AutoField(primary_key=True)
    DsAficion = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.DsAficion


class mPersona(models.Model):
    CvPersona = models.AutoField(primary_key=True)
    Nombre = models.ForeignKey(cNombre, on_delete=models.DO_NOTHING, null=True, blank=True)
    ApePat = models.ForeignKey(cApePat, on_delete=models.DO_NOTHING, null=True, blank=True)
    ApeMat = models.ForeignKey(cApeMat, on_delete=models.DO_NOTHING, null=True, blank=True)
    Aficion = models.ForeignKey(cAficion, on_delete=models.DO_NOTHING, null=True, blank=True)
    Direccion = models.TextField(max_length=100, null=True, blank=True)
    Telefono = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('G', '39 tipos de geis')], default='M')
    Trabajo = models.CharField(max_length=100, null=True, blank=True)
    FecNac = models.DateTimeField(null=True, blank=True)
    TpPerson = models.CharField(max_length=1, choices=[('C', 'Cliente'), ('P', 'Proveedor'), ('E', 'Empleado')], default='N')

    def __str__(self):
        return f"{self.Nombre.DsNombre} {self.ApePat.DsApePat} {self.ApeMat.DsApeMat}"

class cCalle(models.Model):
    CvCalle = models.AutoField(primary_key=True)
    DsCalle = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.DsCalle

class cColonia(models.Model):
    CvColonia = models.AutoField(primary_key=True)
    DsColonia = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.DsColonia

class cMunicipio(models.Model):
    CvMunicipio = models.AutoField(primary_key=True)
    DsMunicipio = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.DsMunicipio

class cCiudad(models.Model):
    CvCiudad = models.AutoField(primary_key=True)
    DsCiudad = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.DsCiudad

class mDireccion(models.Model):
    CvDireccion = models.AutoField(primary_key=True)
    Calle = models.ForeignKey(cCalle, on_delete=models.DO_NOTHING, null=True, blank=True)
    Numero = models.IntegerField(null=True, blank=True)
    Colonia = models.ForeignKey(cColonia, on_delete=models.DO_NOTHING, null=True, blank=True)
    Municipio = models.ForeignKey(cMunicipio, on_delete=models.DO_NOTHING, null=True, blank=True)
    Ciudad = models.ForeignKey(cCiudad, on_delete=models.DO_NOTHING, null=True, blank=True)
    CodPos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.Calle.DsCalle} {self.Colonia.DsColonia} {self.Ciudad.DsCiudad} {self.Municipio.DsMunicipio}"