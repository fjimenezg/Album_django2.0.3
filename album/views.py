from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from album.models import Category, Photo
from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import CategorySerializer, PhotoSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


# Create your views here.
@login_required
def first_view(request):
    #return HttpResponse("<H1>HOLA MUNDO DESDE LA VISTA first_view</H1>")
    return render(request, 'base.html')

@login_required
def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request, 'album/category.html', context)

@login_required
def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'object': category}
    return render(request, 'album/category_detail.html', context)

class PhotoListView(ListView):
    model = Photo

@method_decorator(login_required, name='dispatch')
class PhotoDetailView(DetailView):
    model = Photo

class PhotoUpdate(UpdateView):
    model = Photo
    fields = '__all__' 

class PhotoCreate(CreateView):
    model = Photo
    fields = '__all__'

class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__' 

class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')