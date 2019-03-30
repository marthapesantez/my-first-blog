##Todas las líneas que comienzan con from o import son líneas para agregar algo de otros archivos. 
from django.db import models
from django.utils import timezone


#class Post(models.Model):, esta línea define nuestro modelo (es un objeto).

#class es una palabra clave que indica que estamos definiendo un objeto.
#Post es el nombre de nuestro modelo. Podemos darle un nombre diferente (pero debemos evitar espacios en blanco y caracteres especiales). Siempre inicia el nombre de una clase con una letra mayúscula.
#models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
#llamamos a una funcion que publicara nuestro metodo
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title