from django.db import models

class Movie(models.Model):
    Título = models.CharField(max_length=255)
    Año = models.IntegerField()
    Director = models.CharField(max_length=255)
    Categoría = models.CharField(max_length=100)
    Sinapsis = models.TextField()
    imagen = models.ImageField(upload_to='movies/', null=True, blank=True)

    def __str__(self):
        return f"{self.Título} - {self.Año}"
