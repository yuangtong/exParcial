from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Creacion de variables para la plantilla
lista_tareas = []

# Create your views here.
def index(request):
    return render(request, "index.html")

def inicio(request):
    return render(request, "index.html")

def nuevaTarea(request):
    if request.method == 'POST':
        print(request.POST)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_fin = request.POST.get('fecha_fin')
        estado = request.POST.get('estado')
        responsable = request.POST.get('responsable')
        lista_tareas.append({'nombre': nombre, 'descripcion': descripcion, 'fecha_fin': fecha_fin, 'estado': estado, 'responsable': responsable})
        return HttpResponseRedirect(reverse('inicio'))
    else:
        return render(request, "nuevaTarea.html")

def crearTarea(request):
    global lista_tareas
    tarea = request.POST['tarea']
    lista_tareas.append(tarea)
    return render(request, "index.html", {'tareas': lista_tareas})