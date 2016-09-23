from django.shortcuts import render

# Create your views here.

def Listar_articulos(request):
        return render(request, 'blog/Listar_articulos.html', {})
