from django.db import models

class Familiar(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    edad = models.IntegerField()
    year= models.IntegerField()
    month=models.IntegerField()
    day=models.IntegerField()


    def __str__(self):
        return f"Nombre: {self.name} | Apellido: {self.last_name} | Edad: {self.edad}"
