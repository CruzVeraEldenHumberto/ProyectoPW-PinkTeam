#from django.contrib.auth.models import User 
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import TemplateView
from django.contrib.auth import login, authenticate
from .models import User, Usuario , Materia_Actual, Historial_Materias, Escuela, Grupo, Periodo
from django.http import HttpResponse
from django.core import serializers

from .forms import CustomUserCreationForm
from .forms import Update_Calificacion, RegistroForm
from .forms import UpdateUserForm, CreateUserForm
from .forms import UpdateGrupoForm, CreateGrupoForm
from .forms import UpdateUsuarioForm, CreateUsuarioForm
from .forms import UpdateEscuelaForm, CreateEscuelaForm
from .forms import UpdateMateria_ActualForm, CreateMateria_ActualForm
from .forms import UpdatePeriodoForm, CreatePeriodoForm
from .forms import UpdateHistorial_MateriasForm, CreateHistorial_MateriasForm
from django.db.models import Q

from .filters import BoletaAlumno
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from home.serializers import BoletaSerializer, EscuelaSerializer, Materia_ActualSerializer, UsuarioSerializer
import requests

#from django.shortcuts import get_object_or_404
#from django.conf import settings
# Create your views here.

# Vista inicial con login
class Index(generic.TemplateView):
    template_name = "home/index.html"
   # model = Usuario

#Funcion para redireccionar segun el tipo de usuario
@login_required
def Casa(request):
    user = request.user
    if user.has_perm('home.is_teacher'):
        return redirect(reverse('home:home_docente'))
    elif user.has_perm('home.is_student'):
        return redirect(reverse('home:home_alumno'))
    elif user.has_perm('home.is_admin'):
        return redirect(reverse('home:home_administrador'))
    else:
        return render(request, template_name='home/home_pendiente.html')

#############         Vista Iniciar del docente
@permission_required('home.is_teacher')
def Home_Docente(request):
    status_list = Usuario.objects.all()
    status_filter = status_list.filter(user=request.user)
    return render(request, 'home/home_docente.html',{'filter': status_filter})

#Vista grupo del docente
@permission_required('home.is_teacher')
def Grupo_Docente(request):
    conectedu = Usuario.objects.all()
    filtercu = conectedu.filter(user = request.user)
    status_list = Usuario.objects.all().exclude(user=request.user).order_by("user__last_name")
    return render(request, 'home/grupo_docente.html',{'filter': status_list,'ufilter': filtercu})

class VistaDetalleAlumno(generic.DetailView):
    template_name = "home/detalle_alumno.html"
    model = Usuario

class VistaUpdateCalificacion(generic.UpdateView):
    template_name = "home/update_calificacion.html"
    model = Materia_Actual
    form_class = Update_Calificacion
    success_url = reverse_lazy("home:grupo_docente")




#Vista reporte del docente
@permission_required('home.is_teacher')
def Reporte_Docente(request):
    return render(request, 'home/reporte_docente.html')

#Vista historial del docente
@permission_required('home.is_teacher')
def Historial_Docente(request):
    return render(request, 'home/historial_docente.html')



################          Vista inicial de administrador     #############################
@permission_required('home.is_admin')
def Home_Administrador(request):
    return render(request, 'home/home_administrador.html')

#Vista consulta del administrador
@permission_required('home.is_admin')
def Consulta_Administrador(request):
    return render(request, 'home/consulta_administrador.html')

#Vista historial del administrador
@permission_required('home.is_admin')
def Historial_Administrador(request):
    return render(request, 'home/historial_administrador.html')
    

############################Vistas de la tabla User#########################################
class VistaTablaUser(generic.ListView):
    template_name = "home/tabla_user.html"
    model = User
    queryset = User.objects.all().order_by("id")
    

class VistaDetalleUser(generic.DetailView):
    template_name = "home/detalle_user.html"
    model = User

class VistaUpdateUser(generic.UpdateView):
    template_name = "home/update_user.html"
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy("home:tabla_user")

class VistaDeleteUser(generic.DeleteView):
    template_name = "home/delete_user.html"
    model = User
    success_url = reverse_lazy("home:tabla_user")

def VistaCreateUser(request):
    context = {}
    if request.POST:
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:consulta_administrador')
        else:
            context['signup_form']=form
    else:
        form = RegistroForm()
        context['signup_form']=form
    return render(request, 'home/create_user.html', context)

###########################################################################################GrupoAdmin
class VistaTablaGrupo(generic.ListView):
    template_name = "home/tabla_grupo.html"
    model = Grupo
    queryset = Grupo.objects.all().order_by("id")

class VistaDetalleGrupo(generic.DetailView):
    template_name = "home/detalle_grupo.html"
    model = Grupo

class VistaUpdateGrupo(generic.UpdateView):
    template_name = "home/update_grupo.html"
    model = Grupo
    form_class = UpdateGrupoForm
    success_url = reverse_lazy("home:tabla_grupo")

class VistaDeleteGrupo(generic.DeleteView):
    template_name = "home/delete_grupo.html"
    model = Grupo
    success_url = reverse_lazy("home:tabla_grupo")

class VistaCreateGrupo(generic.CreateView):
    template_name = "home/create_grupo.html"
    model = Grupo
    form_class = CreateGrupoForm
    success_url = reverse_lazy("home:consulta_administrador")
###########################################################################################UsuarioAdmin
class VistaTablaUsuario(generic.ListView):
    template_name = "home/tabla_usuario.html"
    model = Usuario
    queryset = Usuario.objects.all().order_by("id")

class VistaDetalleUsuario(generic.DetailView):
    template_name = "home/detalle_usuario.html"
    model = Usuario

class VistaUpdateUsuario(generic.UpdateView):
    template_name = "home/update_usuario.html"
    model = Usuario
    form_class = UpdateUsuarioForm
    success_url = reverse_lazy("home:tabla_usuario")

class VistaDeleteUsuario(generic.DeleteView):
    template_name = "home/delete_usuario.html"
    model = Usuario
    success_url = reverse_lazy("home:tabla_usuario")

def VistaCreateUsuario(request):
    context = {}
    if request.POST:
        form = CreateUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:consulta_administrador')
        else:
            context['signup_form']=form
    else:
        form = CreateUsuarioForm()
        context['signup_form']=form
    return render(request, 'home/create_usuario.html', context)

###########################################################################################EscuelaAdmin
class VistaTablaEscuela(generic.ListView):
    template_name = "home/tabla_escuela.html"
    model = Escuela
    queryset = Escuela.objects.all().order_by("id")

class VistaDetalleEscuela(generic.DetailView):
    template_name = "home/detalle_escuela.html"
    model = Escuela

class VistaUpdateEscuela(generic.UpdateView):
    template_name = "home/update_escuela.html"
    model = Escuela
    form_class = UpdateEscuelaForm
    success_url = reverse_lazy("home:tabla_escuela")

class VistaDeleteEscuela(generic.DeleteView):
    template_name = "home/delete_escuela.html"
    model = Escuela
    success_url = reverse_lazy("home:tabla_escuela")

def VistaCreateEscuela(request):
    context = {}
    if request.POST:
        form = CreateEscuelaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:consulta_administrador')
        else:
            context['signup_form']=form
    else:
        form = CreateEscuelaForm()
        context['signup_form']=form
    return render(request, 'home/create_escuela.html', context)

###########################################################################################Materia_ActualAdmin
class VistaTablaMateria_Actual(generic.ListView):
    template_name = "home/tabla_materia_Actual.html"
    model = Materia_Actual
    queryset = Materia_Actual.objects.all().order_by("id")

class VistaDetalleMateria_Actual(generic.DetailView):
    template_name = "home/detalle_materia_Actual.html"
    model = Materia_Actual

class VistaUpdateMateria_Actual(generic.UpdateView):
    template_name = "home/update_materia_Actual.html"
    model = Materia_Actual
    form_class = UpdateMateria_ActualForm
    success_url = reverse_lazy("home:tabla_materia_Actual")

class VistaDeleteMateria_Actual(generic.DeleteView):
    template_name = "home/delete_materia_Actual.html"
    model = Materia_Actual
    success_url = reverse_lazy("home:tabla_materia_Actual")

def VistaCreateMateria_Actual(request):
    context = {}
    if request.POST:
        form = CreateMateria_ActualForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:consulta_administrador')
        else:
            context['signup_form']=form
    else:
        form = CreateMateria_ActualForm()
        context['signup_form']=form
    return render(request, 'home/create_materia_Actual.html', context)



###########################################################################################PeriodoAdmin


class VistaTablaPeriodo(generic.ListView):
    template_name = "home/tabla_periodo.html"
    model = Periodo
    queryset = Periodo.objects.all().order_by("id")

class VistaDetallePeriodo(generic.DetailView):
    template_name = "home/detalle_periodo.html"
    model = Periodo

class VistaUpdatePeriodo(generic.UpdateView):
    template_name = "home/update_periodo.html"
    model = Periodo
    form_class = UpdatePeriodoForm
    success_url = reverse_lazy("home:tabla_periodo")

class VistaDeletePeriodo(generic.DeleteView):
    template_name = "home/delete_periodo.html"
    model = Periodo
    success_url = reverse_lazy("home:tabla_periodo")

def VistaCreatePeriodo(request):
    context = {}
    if request.POST:
        form = CreatePeriodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:consulta_administrador')
        else:
            context['signup_form']=form
    else:
        form = CreatePeriodoForm()
        context['signup_form']=form
    return render(request, 'home/create_periodo.html', context)


###########################################################################################historial_MateriasAdmin


class VistaTablaHistorial_Materias(generic.ListView):
    template_name = "home/tabla_historial_Materias.html"
    model = Historial_Materias
    queryset = Historial_Materias.objects.all().order_by("id")

class VistaDetalleHistorial_Materias(generic.DetailView):
    template_name = "home/detalle_historial_Materias.html"
    model = Historial_Materias

class VistaUpdateHistorial_Materias(generic.UpdateView):
    template_name = "home/update_historial_Materias.html"
    model = Historial_Materias
    form_class = UpdateHistorial_MateriasForm
    success_url = reverse_lazy("home:tabla_historial_Materias")

class VistaDeleteHistorial_Materias(generic.DeleteView):
    template_name = "home/delete_historial_Materias.html"
    model = Historial_Materias
    success_url = reverse_lazy("home:tabla_historial_Materias")

def VistaCreateHistorial_Materias(request):
    context = {}
    if request.POST:
        form = CreateHistorial_MateriasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:consulta_administrador')
        else:
            context['signup_form']=form
    else:
        form = CreateHistorial_MateriasForm()
        context['signup_form']=form
    return render(request, 'home/create_historial_Materias.html', context)

    








#Funcion para crear nuevo usuario
# class Signup(generic.CreateView):
#     template_name = "home/signup.html"
#     form_class = RegistroForm

#     def get_success_url(self):
#         return reverse('home:index')

def Signup(request):
    context = {}
    if request.POST:
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
        else:
            context['signup_form']=form
    else:
        form = RegistroForm()
        context['signup_form']=form
    return render(request, 'home/signup.html', context)


    

#Funcion para Error 404 (Page not Found)
class Error404View(TemplateView):
    template_name = "base/base2.html"


#########################################################################     VISTAS DEL ALUMNOS     
@permission_required('home.is_student')
def Home_Alumno(request):
    queryset = Usuario.objects.all()
    status_filter = queryset.filter(user=request.user)
    query_filter = Escuela.objects.all()
    status_fil = query_filter.filter()
    return render(request, 'home/home_alumno.html', {'filter':status_filter,'filterU':status_fil})

############################################################################  VISTA DEL AVANCE
#######  VISTA DEL AVANCE DEL CICLO DEL ESTUDIANTES 
@permission_required('home.is_student')
def Avance_Alumno(request):
    status_list = Usuario.objects.all()
    status_fil = status_list.filter(user=request.user)
    query_filter = Materia_Actual.objects.all()
    status_filter = query_filter.filter()
    return render(request, 'home/avance_alumno.html',{'filter':status_filter, 'filterU':status_fil})  
   # , pk
   # user_pk= User.objects.get(pk=pk)
   #,context={'user':user_pk}
############################################################################   HISTORIAL ALUMNO 
#Vista historial del alumno Historial_Materias
@permission_required('home.is_student')
def Historial_Alumno(request):
    status_list = Usuario.objects.all()
    status_fil = status_list.filter(user=request.user)
    queryset= Historial_Materias.objects.all()
    status_filter = queryset.filter()
    querysetp= Periodo.objects.all()
    status_filter_p = querysetp.filter()
    return render(request,'home/historial_alumno.html', {'filter':status_filter, 'filterU':status_fil, 'filterP':status_filter_p})

#############################################################   IMPRIME MANUAL DE IMPRIMIR BOLETA 
@permission_required('home.is_student')
def Imprimir_Alumno(request):
    queryset = Usuario.objects.all()
    status_filter = queryset.filter(user=request.user)
    return render(request, 'home/imprimir_alumno.html', {'filter':status_filter})

##########################AQUI EMPIZAN LAS API
def wsBoleta(request):
    data = serializers.serialize("json", Materia_Actual.objects.all())
    return HttpResponse(data, content_type="application/json")

def wsAlumno(request):
    url = "http://localhost:8000/v1/lista_alumno/" ##
    response = requests.get(url)
    response = response.json()

    context = {
        "object_list": response
    }
    return render(request, "Alumno/detalle_alumno.html", context)

@api_view(["GET", "POST"])
def Lista_Alumno(request):
    #List
    if request.method == "GET":
        queryset = Materia_Actual.objects.all()
        data = BoletaSerializer(queryset, many = True)
        return Response(data.data, status = status.HTTP_200_OK)
    #Create
    elif request.method =="POST":
        data = BoletaSerializer(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status = status.HTTP_201_CREATED)
        return Response(data.errors, status = status.HTTP_400_BAD_REQUEST)
#

@api_view(["GET", "PUT"])
def detail_update_alumno(request, pk=None):
    queryset = Materia_Actual.objects.filter(id=pk).first()
    if queryset:
        #detail
        if request.method == "GET":
            data = BoletaSerializer(queryset)
            return Response(data.data, status=status.HTTP_200_OK)
        #Update
        elif request.method == "PUT":
            data = BoletaSerializer(queryset, data = request.data)
            if data.is_valid():
                data.save()
                return Response(data.data)
            return Response(data.errors, status = status.HTTP_400_BAD_REQUEST)
        #Delete
        # elif request.method == "DELETE":
        #     queryset.delete()
        #     return Response({"message": "Student Destroy Successsfull"}, status=status.HTTP_200_OK)
    return Response({"message": "Student Not Found"}, status=status.HTTP_400_BAD_REQUEST)


class Grupo_API(generic.ListView):
    model = Usuario
    template_name = "Alumno/grupo_docente.html"
    
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BoletaAlumno(self.request.GET, queryset=self.get_queryset())
        return context

    # def get_queryset(self):
    #      return Usuario.objects.all().order_by("grupo", "user__last_name")

    # def get_queryset(self):
    #     query = self.request.GET.get('search')
    #     filter_field = self.request.GET.get('filter_field')
    
    #     if filter_field == "all":
    #         return Usuario.objects.filter(
    #             Q(user__username__icontains=query)
    #         ).order_by("grupo", "user__last_name")

    #     else:
    #         return Usuario.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     context['form'] = FilterForm(initial= {
    #         'search': self.request.GET.get('search',''),
    #         'filter_field': self.request.GET.get('filter_field',''),
    #     })

    #     return context

class API_Alumno(generic.DetailView):
    template_name = "Alumno/detalle_alumno.html"
    model = Usuario


@api_view(["GET", "POST"])
def List_Escuela(request):
    #list
    if request.method == "GET":
        queryset = Escuela.objects.all()
        data = EscuelaSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
    #create
    elif request.method == "POST":
        data = EscuelaSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


def wsCliente(request):
    url = "https://pinkschool.herokuapp.com/v1/list_escuela/"
    response = requests.get(url)
    response = response.json()
    context = {
        "object_list": response
    }
    return render(request, "home/wsEscuela.html", context)



#### nuevas apis
#API Detail de un alumno de sus materias
@api_view(["GET"])
def Detail_Materia_Actual(request, pk=None):
    if request.method == "GET":
        queryset = Materia_Actual.objects.filter(alumno=pk).all()
        data = Materia_ActualSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def List_Usuario(request):
    if request.method == "GET":
        queryset = Usuario.objects.all().order_by("grado_alumno","curp")
        data = UsuarioSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

def wsMateria_Actual(request, pk=None):
    url = "https://pinkschool.herokuapp.com/v1/detail_materia_actual/" + str(pk) + "/"
    response = requests.get(url)
    response = response.json()
    context = {
        "object_list": response
    }
    return render(request, "home/wsMateriaActual.html", context)

def wsUsuario(request):
    url = "https://pinkschool.herokuapp.com/v1/list_usuario/"
    response = requests.get(url)
    response = response.json()
    context = {
        "object_list": response
    }
    return render(request, "home/wsUsuario.html", context)



#Metodo buscar

#####################################################################################


from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION

def main(request):

    logs = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20]
    logCount = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20].count()

    return render(request, 'home/historialgeneral.html', {"logs":logs, "logCount":logCount})
      
    