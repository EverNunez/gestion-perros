from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Perro, Cruce
from .forms import PerroForm, CruceForm
from datetime import date, timedelta

def inicio(request):
    return render(request, "perros/inicio.html")

def lista_perros(request):
    perros = Perro.objects.all()
    return render(request, "perros/lista_perros.html", {"perros": perros})

def agregar_perro(request):
    if request.method == "POST":
        form = PerroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_perros")
    else:
        form = PerroForm()
    return render(request, "perros/agregar_perro.html", {"form": form})

def eliminar_perro(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    perro.delete()
    return redirect("lista_perros")

def detalle_perro(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    cruces = perro.cruces.all()

    for cruce in cruces:
        cruce.dias_transcurridos = (date.today() - cruce.fecha_insem).days
        cruce.fecha_parto_estimada = cruce.fecha_insem + timedelta(days=63)
        cruce.save()

    return render(request, "perros/detalle_perro.html", {"perro": perro, "cruces": cruces})

def agregar_cruce(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    if request.method == "POST":
        form = CruceForm(request.POST)
        if form.is_valid():
            cruce = form.save(commit=False)
            cruce.perro = perro
            cruce.save()
            return redirect("detalle_perro", perro_id=perro.id)
        else:
            # Si el formulario no es válido
            return render(request, "perros/agregar_cruce.html", {"form": form, "perro": perro, "error": "Formulario no válido."})
    else:
        form = CruceForm()
    return render(request, "perros/agregar_cruce.html", {"form": form, "perro": perro})

def editar_cruce(request, cruce_id):
    cruce = get_object_or_404(Cruce, id=cruce_id)
    if request.method == "POST":
        form = CruceForm(request.POST, instance=cruce)
        if form.is_valid():
            form.save()
            return redirect("detalle_perro", perro_id=cruce.perro.id)
    else:
        form = CruceForm(instance=cruce)
    return render(request, "perros/editar_cruce.html", {"form": form, "cruce": cruce})

def eliminar_cruce(request, cruce_id):
    cruce = get_object_or_404(Cruce, id=cruce_id)
    perro_id = cruce.perro.id
    cruce.delete()
    return redirect("detalle_perro", perro_id=perro_id)

