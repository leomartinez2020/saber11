from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Colegio(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    codinst = models.CharField(max_length=20, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    codigomunicipio = models.IntegerField(blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    calendario = models.CharField(max_length=2, blank=True, null=True)
    naturaleza = models.CharField(max_length=30, blank=True, null=True)
    evaluados = models.IntegerField(blank=True, null=True)
    matematicas = models.FloatField(blank=True, null=True)
    sociales = models.FloatField(blank=True, null=True)
    ingles = models.FloatField(blank=True, null=True)
    ciencias = models.FloatField(blank=True, null=True)
    lectura = models.FloatField(blank=True, null=True)
    jornada = models.CharField(max_length=50, blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    promponderado = models.FloatField(blank=True, null=True)
    puntajeglobal = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        suma = ((self.matematicas + self.sociales + self.ciencias + self.lectura) * 3 + self.ingles)
        self.promponderado = suma / 13.0
        self.puntajeglobal = round(self.promponderado * 5, 2)
        self.slug = slugify(self.nombre)
        super(Colegio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detalle_colegio', kwargs={'pk': self.pk, 'slug': self.slug})

class Colegio2020(Colegio):

    def save(self, *args, **kwargs):
        suma = ((self.matematicas + self.sociales + self.ciencias + self.lectura) * 3 + self.ingles)
        self.promponderado = suma / 13.0
        self.puntajeglobal = round(self.promponderado * 5, 2)
        self.slug = slugify(self.nombre)
        super(Colegio2020, self).save(*args, **kwargs)

    class Meta:
        db_table = 'saber2020A'
