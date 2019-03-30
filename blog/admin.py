from django.contrib import admin
#importamos (incluimos) el modelo Post definido en el capítulo anterior. 
from .models import Post
#Para hacer nuestro modelo visible en la página del administrador, tenemos que registrar el modelo con 
admin.site.register(Post)