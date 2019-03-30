#Como puedes ver, hemos creado una función (def)
#llamada post_list que acepta request y return una función render que reproduce (construye) nuestra plantilla blog/post_list.html.
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
