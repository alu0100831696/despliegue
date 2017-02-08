from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from restaurantes.models import Restaurantes
from restaurantes.forms import formAdd

import json

@login_required(login_url='/accounts/login/')
def index(request):
    form = formAdd()
    return render(request,'restaurantes.html', {'form':form})

def test(request):
    return render(request,'test.html', {})

@login_required
def loadRestaurants(request):
    loadR=Restaurantes()
    return HttpResponse(loadR.showRestaurants())

#https://www.tutorialspoint.com/django/django_form_processing.htm     http://pythoncentral.io/how-to-use-python-django-forms/

def addRestaurants(request):

    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
   
        form = formAdd(request.POST) # Bind data from request.POST into a PostForm
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            return JsonResponse({'mensaje':form.save()})
        else:
            return JsonResponse(form.errors, status=500)

        return JsonResponse({'ok':"AS"})

def delRestaurants(request):
    
    delR=Restaurantes()
    id=request.GET['id']
    assert(id)
    delR.delRestaurants(id)
    return JsonResponse({'mensaje':"Eliminado correctamente"}, status=200)

def updateRestaurants (request):

    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = formAdd(request.POST) 
     # If data is valid, proceeds to create a new post and redirect the user
    if form.is_valid():
        return JsonResponse({'mensaje':form.update()})
    else:
        return JsonResponse(form.errors, status=500)
