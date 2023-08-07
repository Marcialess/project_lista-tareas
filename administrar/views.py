from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrar.models import Tarea


def v_index(request):
  if request.method == 'POST':
    _titulo = request.POST['titulo']
    tarea = Tarea()
    tarea.titulo = _titulo
    print(tarea.estado)
    tarea.save()
    return HttpResponseRedirect("/")
  else:

    consulta = Tarea.objects.filter(titulo__icontains = request.GET.get("titulo",         ""))
  
    
    context = {
    'var1':'valortest',
    'var2':'secondvalor',
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




  