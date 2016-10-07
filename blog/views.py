#from django.shortcuts import render
#from .models import Postear
#from django.utils import timezone

# Create your views here.

#def Listar_articulos(request):
#    postear = Postear.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/Listar_articulos.html', {'postear':postear})

from django.shortcuts import render
from django.utils import timezone
from .models import Postear
from django.shortcuts import render, get_object_or_404

def Listar_articulos(request):
    posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/Listar_articulos.html', {'posts': posts})


def post_detail(request, pk):
    posts = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/post_detail.html', {'posts': posts})
