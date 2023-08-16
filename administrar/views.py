from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrar.models import Tarea
from .forms import TareaForm


def v_index(request):
  if request.method == 'POST':  
    _titulo = request.POST['titulo']
  
    datos = request.POST.copy()
    
    form= TareaForm(datos)
    if form.is_valid():

      form.save()

    else:
            
      return HttpResponseRedirect("/")
  
  else:
    consulta = Tarea.objects.filter(titulo__icontains = request.GET.get("titulo",""))

    
    if request.GET.get("estado","") != "":
      consulta = consulta.filter(estado = request.GET.get("estado",""))
      
      
    context = {
    'lista': consulta
  }
  return render(request,'index.html', context)


def v_eliminar(request, tarea_id):
  Tarea.objects.filter(id= tarea_id).delete()
  return HttpResponseRedirect("/")


def v_completado(request, tarea_id):
  task = Tarea.objects.get(id=tarea_id)
  task.status = 1
  task.save()
  return HttpResponseRedirect('/')

def v_login(request):
  from .forms import LoginForm #importando el formulario
  from django.contrib.auth import authenticate, login
  
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid(): #verifica los datos que necesita
      user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data["password"]) 
      if user is not None:
        login(request, user)
        return HttpResponseRedirect("/")
      else:
        return HttpResponseRedirect("/")
    else:
    #los datos no son correctos
      return HttpResponseRedirect("/")
  else:
    context = {
      "form": LoginForm(request.POST) #envio un formal html
    }
  return render(request, "login.html", context)

def v_logout(request):

  from django.contrib.auth import logout

 

  if request.user.is_authenticated:

    logout(request) # Aqui se cierra la sesion

 

  return HttpResponseRedirect("/")





  