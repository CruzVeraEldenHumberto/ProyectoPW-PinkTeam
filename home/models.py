from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import User
from datetime import datetime    
from django.utils.translation import ugettext as _
#buscar como pasar multiples campos en def_str
#nos aseguramos que los nombres de usuario sea facil identificar que rol tienen
class User(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    pass

class Grupo(models.Model):
    nombre_grupo=models.CharField(max_length=50)
    turno=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_grupo

class Usuario(models.Model):
    MS_GRADOS = (
        ("Primer grado", "Primer grado"),
        ("Segundo grado","Segundo grado"),
        ("Tercer grado","Tercer grado"),
        ("Cuarto grado","Cuarto grado"),
        ("Quinto grado","Quinto grado"),
        ("Sexto grado","Sexto grado"),
        ("Pendiente","Pendiente"),
    )

    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono_casa = models.CharField(max_length=32, default="pendiente")
    telefono_cel = models.CharField(max_length=32, default="pendiente")
    titulo_docente = models.CharField(max_length=50, default="pendiente")
    grado_alumno = models.CharField(max_length=20, choices = MS_GRADOS, default="Pendiente")
    curp = models.CharField(max_length=20, default="pendiente")
    direccion = models.CharField(max_length=50, default="pendiente")
    fecha_nacimiento = models.DateTimeField(default=datetime.now, blank=True)
    register_timestamp = models.DateTimeField(auto_now_add=True)
    register_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

# Se agregan permisos a la clase Usuario
    class Meta:
        permissions = (
            ('is_teacher', _('Is Teacher')),
            ('is_student', _('Is Student')),
            ('is_admin', _('Is Admin')),
        )

class Escuela(models.Model):
    nombre_institucion=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    nivel_educativo=models.CharField(max_length=20)
    control=models.CharField(max_length=30)
    turno=models.CharField(max_length=10)
    clave=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_institucion

class Materia_Actual(models.Model):
    MS_MATERIAS = (
        #grado 1
        ("Espa??ol 1", "Espa??ol 1"),
        ("Matem??ticas 1","Matem??ticas 1"),
        ("Exploraci??n de la Naturaleza y la Sociedad 1","Exploraci??n de la Naturaleza y la Sociedad 1"),
        ("Formaci??n C??vica y ??tica 1","Formaci??n C??vica y ??tica 1"),
        #grado 2
        ("Espa??ol 2", "Espa??ol 2"),
        ("Matem??ticas 2","Matem??ticas 2"),
        ("Exploraci??n de la Naturaleza y la Sociedad 2","Exploraci??n de la Naturaleza y la Sociedad 2"),
        ("Formaci??n C??vica y ??tica 2","Formaci??n C??vica y ??tica 2"),
        #grado 3
        ("Espa??ol 3", "Espa??ol 3"),
        ("Matem??ticas 3","Matem??ticas 3"),
        ("Ciencias Naturales 1","Ciencias Naturales 1"),
        ("La Entidad donde vivo","La Entidad donde vivo"),
        ("Formaci??n C??vica y ??tica 3","Formaci??n C??vica y ??tica 3"),
        #grado 4
        ("Espa??ol 4", "Espa??ol 4"),
        ("Matem??ticas 4","Matem??ticas 4"),
        ("Ciencias Naturales 2","Ciencias Naturales 2"),
        ("Geograf??a 1","Geograf??a 1"),
        ("Historia 1","Historia 1"),
        ("Formaci??n C??vica y ??tica 4","Formaci??n C??vica y ??tica 4"),
        #grado 5
        ("Espa??ol 5", "Espa??ol 5"),
        ("Matem??ticas 5","Matem??ticas 5"),
        ("Ciencias Naturales 3","Ciencias Naturales 3"),
        ("Geograf??a 2","Geograf??a 2"),
        ("Historia 2","Historia 2"),
        ("Formaci??n C??vica y ??tica 5","Formaci??n C??vica y ??tica 5"),
        #grado 6
        ("Espa??ol 6", "Espa??ol 6"),
        ("Matem??ticas 6","Matem??ticas 6"),
        ("Ciencias Naturales 4","Ciencias Naturales 4"),
        ("Geograf??a 3","Geograf??a 3"),
        ("Historia 3","Historia 3"),
        ("Formaci??n C??vica y ??tica 6","Formaci??n C??vica y ??tica 6"),
        ("Pendiente","Pendiente"),
    )
    MS_HORARIOS = (
        #matutinos
        ("8:00-9:00", "8:00-9:00"),
        ("9:00-10:00", "9:00-10:00"),
        ("10:00-11:00", "10:00-11:00"),
        ("11:30-12:30", "11:30-12:30"),
        ("12:30-13:30", "12:30-13:30"),
        ("13:30-14:30", "13:30-14:30"),
        #vespertinos
        ("13:30-14:00", "13:30-14:00"),
        ("14:00-15:00", "14:00-15:00"),
        ("15:00-16:00", "15:00-16:00"),
        ("16:30-17:00", "16:00-17:00"),
        ("17:00-18:30", "17:30-18:30"),
        ("18:30-19:30", "17:30-18:30"),
        ("Pendiente","Pendiente"),
    )
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_materia=models.CharField(max_length=50, choices = MS_MATERIAS, default="Pendiente")
    horario=models.CharField(max_length=50, choices = MS_HORARIOS, default="Pendiente")
    b1=models.FloatField(default=0.0)
    b2=models.FloatField(default=0.0)
    b3=models.FloatField(default=0.0)
    b4=models.FloatField(default=0.0)
    b5=models.FloatField(default=0.0)
    promedio=models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre_materia

class Periodo(models.Model):
    nombre_periodo=models.CharField(max_length=40)
    inicio_periodo=models.CharField(max_length=30)
    fin_periodo=models.CharField(max_length=30)
   
    def __str__(self):
        return self.nombre_periodo

class Historial_Materias(models.Model):
    MS_MATERIAS = (
        #grado 1
        ("Espa??ol 1", "Espa??ol 1"),
        ("Matem??ticas 1","Matem??ticas 1"),
        ("Exploraci??n de la Naturaleza y la Sociedad 1","Exploraci??n de la Naturaleza y la Sociedad 1"),
        ("Formaci??n C??vica y ??tica 1","Formaci??n C??vica y ??tica 1"),
        #grado 2
        ("Espa??ol 2", "Espa??ol 2"),
        ("Matem??ticas 2","Matem??ticas 2"),
        ("Exploraci??n de la Naturaleza y la Sociedad 2","Exploraci??n de la Naturaleza y la Sociedad 2"),
        ("Formaci??n C??vica y ??tica 2","Formaci??n C??vica y ??tica 2"),
        #grado 3
        ("Espa??ol 3", "Espa??ol 3"),
        ("Matem??ticas 3","Matem??ticas 3"),
        ("Ciencias Naturales 1","Ciencias Naturales 1"),
        ("La Entidad donde vivo","La Entidad donde vivo"),
        ("Formaci??n C??vica y ??tica 3","Formaci??n C??vica y ??tica 3"),
        #grado 4
        ("Espa??ol 4", "Espa??ol 4"),
        ("Matem??ticas 4","Matem??ticas 4"),
        ("Ciencias Naturales 2","Ciencias Naturales 2"),
        ("Geograf??a 1","Geograf??a 1"),
        ("Historia 1","Historia 1"),
        ("Formaci??n C??vica y ??tica 4","Formaci??n C??vica y ??tica 4"),
        #grado 5
        ("Espa??ol 5", "Espa??ol 5"),
        ("Matem??ticas 5","Matem??ticas 5"),
        ("Ciencias Naturales 3","Ciencias Naturales 3"),
        ("Geograf??a 2","Geograf??a 2"),
        ("Historia 2","Historia 2"),
        ("Formaci??n C??vica y ??tica 5","Formaci??n C??vica y ??tica 5"),
        #grado 6
        ("Espa??ol 6", "Espa??ol 6"),
        ("Matem??ticas 6","Matem??ticas 6"),
        ("Ciencias Naturales 4","Ciencias Naturales 4"),
        ("Geograf??a 3","Geograf??a 3"),
        ("Historia 3","Historia 3"),
        ("Formaci??n C??vica y ??tica 6","Formaci??n C??vica y ??tica 6"),
        ("Pendiente","Pendiente"),
    )
    MS_HORARIOS = (
        #matutinos
        ("8:00-9:00", "8:00-9:00"),
        ("9:00-10:00", "9:00-10:00"),
        ("10:00-11:00", "10:00-11:00"),
        ("11:30-12:30", "11:30-12:30"),
        ("12:30-13:30", "12:30-13:30"),
        ("13:30-14:30", "13:30-14:30"),
        #vespertinos
        ("13:30-14:00", "13:30-14:00"),
        ("14:00-15:00", "14:00-15:00"),
        ("15:00-16:00", "15:00-16:00"),
        ("16:30-17:00", "16:00-17:00"),
        ("17:00-18:30", "17:30-18:30"),
        ("18:30-19:30", "17:30-18:30"),
        ("Pendiente","Pendiente"),
    )
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_materia=models.CharField(max_length=50, choices = MS_MATERIAS, default="Pendiente")
    horario=models.CharField(max_length=50, choices = MS_HORARIOS, default="Pendiente")
    b1=models.FloatField(default=0.0)
    b2=models.FloatField(default=0.0)
    b3=models.FloatField(default=0.0)
    b4=models.FloatField(default=0.0)
    b5=models.FloatField(default=0.0)
    promedio=models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre_materia