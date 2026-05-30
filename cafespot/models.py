from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class Rol(models.Model):
    rol = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.rol

    # Adaugă acest bloc pentru traducere
    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roluri"

class Utilizator(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)
    cafenele_favorite = models.ManyToManyField('Cafenea', related_name='favorizata_de', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Utilizator"
        verbose_name_plural = "Utilizatori"

class Cafenea(models.Model):
    nume = models.CharField(max_length=100)
    adresa = models.CharField(max_length=255)
    latitudine = models.DecimalField(max_digits=10, decimal_places=8)
    longitudine = models.DecimalField(max_digits=11, decimal_places=8)
    descriere = models.CharField(max_length=255)
    program = models.CharField(max_length=255, blank=True, null=True)
    imagine = models.ImageField(upload_to='cafespot', blank=True, null=True)
    utilizatori_care_au_favorizat = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite', blank=True)

    def __str__(self):
        return self.nume


    class Meta:
        verbose_name = "Cafenea"
        verbose_name_plural = "Cafenele"

class Recenzie(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentariu = models.CharField(max_length=255)
    data_publicarii = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Utilizator, on_delete=models.CASCADE, related_name='recenzii_scrise')
    cafe = models.ForeignKey(Cafenea, on_delete=models.CASCADE, related_name='recenzii')

    def __str__(self):
        return f"Recenzie {self.rating}/5 - {self.cafe.nume}"

    class Meta:
        verbose_name = "Recenzie"
        verbose_name_plural = "Recenzii"