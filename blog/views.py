#Como puedes ver, hemos creado una función (def)
#llamada post_list que acepta request y return una función render que reproduce (construye) nuestra plantilla blog/post_list.html.
from django.shortcuts import render
# punto antes de models indica el directorio actual o la aplicación actual. Ambos, views.py y models.py están en el mismo directorio.
#Esto significa que podemos utilizar . y el nombre del archivo (sin .py). Ahora importamos el nombre del modelo (Post).
from .models import Post
from django.utils import timezone

#request (todo lo que recibimos del usuario via Internet)
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#El último parámetro, que se ve así: {} es un lugar en el que podemos agregar algunas cosas para que la plantilla las use. 
#Necesitamos nombrarlos (los seguiremos llamando 'posts' por ahora). :) Se debería ver así: {'posts': posts}. Fíjate en que la parte antes de : es una cadena; tienes que envolverla con comillas: ".
	return render(request, 'blog/post_list.html', {'posts': posts})
