#from django.shortcuts import render
#from .models import Postear
#from django.utils import timezone

# Create your views here.

#def Listar_articulos(request):
#    postear = Postear.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/Listar_articulos.html', {'postear':postear})

from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import Postear
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def Listar_articulos(request):
    posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/Listar_articulos.html', {'posts': posts})

def post_detail(request, pk):
    posts = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': posts})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.fecha_publicacion = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
