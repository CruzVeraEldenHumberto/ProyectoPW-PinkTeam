from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import permission_required
from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    # path('avance_alumno/', views.Avance_Alumno, name="avance_alumno"),
    path('home_docente/', views.Home_Docente, name='home_docente'),
    path('grupo_docente/', views.Grupo_Docente, name="grupo_docente"),
    path('detalle_alumno/<int:pk>/', permission_required('home.is_teacher')(views.VistaDetalleAlumno.as_view()), name="detalle_alumno"),
    path('update_calificacion/<int:pk>/', permission_required('home.is_teacher')(views.VistaUpdateCalificacion.as_view()), name="update_calificacion"),
    path('historial_docente/', views.Historial_Docente, name="historial_docente"),
    path('reporte_docente/', views.Reporte_Docente, name="reporte_docente"),
    path('home_administrador/', views.Home_Administrador, name="home_administrador"),
    path('historial_administrador/', views.Historial_Administrador, name="historial_administrador"),
    path('consulta_administrador/', views.Consulta_Administrador, name="consulta_administrador"),
    #URL administrador

    
    ##Desde aqui inicial las de admin
    ##user
    path('tabla_user/', permission_required('home.is_admin')(views.VistaTablaUser.as_view()), name="tabla_user"),
    path('detalle_user/<int:pk>/', permission_required('home.is_admin')(views.VistaDetalleUser.as_view()), name="detalle_user"),
    path('update_user/<int:pk>/', permission_required('home.is_admin')(views.VistaUpdateUser.as_view()), name="update_user"),
    path('delete_user/<int:pk>/', permission_required('home.is_admin')(views.VistaDeleteUser.as_view()), name="delete_user"),
    path('create_user/', permission_required('home.is_admin')(views.VistaCreateUser), name="create_user"),

    ##grupo
    path('tabla_grupo/', permission_required('home.is_admin')(views.VistaTablaGrupo.as_view()), name="tabla_grupo"),
    path('detalle_grupo/<int:pk>/', permission_required('home.is_admin')(views.VistaDetalleGrupo.as_view()), name="detalle_grupo"),
    path('update_grupo/<int:pk>/', permission_required('home.is_admin')(views.VistaUpdateGrupo.as_view()), name="update_grupo"),
    path('delete_grupo/<int:pk>/', permission_required('home.is_admin')(views.VistaDeleteGrupo.as_view()), name="delete_grupo"),
    path('create_grupo/', permission_required('home.is_admin')(views.VistaCreateGrupo.as_view()), name="create_grupo"),

    ##Usuario
    path('tabla_usuario/', permission_required('home.is_admin')(views.VistaTablaUsuario.as_view()), name="tabla_usuario"),
    path('detalle_usuario/<int:pk>/', permission_required('home.is_admin')(views.VistaDetalleUsuario.as_view()), name="detalle_usuario"),
    path('update_usuario/<int:pk>/', permission_required('home.is_admin')(views.VistaUpdateUsuario.as_view()), name="update_usuario"),
    path('delete_usuario/<int:pk>/', permission_required('home.is_admin')(views.VistaDeleteUsuario.as_view()), name="delete_usuario"),
    path('create_usuario/', permission_required('home.is_admin')(views.VistaCreateUsuario), name="create_usuario"),

    ##Escuela
    path('tabla_escuela/', permission_required('home.is_admin')(views.VistaTablaEscuela.as_view()), name="tabla_escuela"),
    path('detalle_escuela/<int:pk>/', permission_required('home.is_admin')(views.VistaDetalleEscuela.as_view()), name="detalle_escuela"),
    path('update_escuela/<int:pk>/', permission_required('home.is_admin')(views.VistaUpdateEscuela.as_view()), name="update_escuela"),
    path('delete_escuela/<int:pk>/', permission_required('home.is_admin')(views.VistaDeleteEscuela.as_view()), name="delete_escuela"),
    path('create_escuela/', permission_required('home.is_admin')(views.VistaCreateEscuela), name="create_escuela"),

    ##materia_Actual
    path('tabla_materia_Actual/', permission_required('home.is_admin')(views.VistaTablaMateria_Actual.as_view()), name="tabla_materia_Actual"),
    path('detalle_materia_Actual/<int:pk>/', permission_required('home.is_admin')(views.VistaDetalleMateria_Actual.as_view()), name="detalle_materia_Actual"),
    path('update_materia_Actual/<int:pk>/', permission_required('home.is_admin')(views.VistaUpdateMateria_Actual.as_view()), name="update_materia_Actual"),
    path('delete_materia_Actual/<int:pk>/', permission_required('home.is_admin')(views.VistaDeleteMateria_Actual.as_view()), name="delete_materia_Actual"),
    path('create_materia_Actual/', permission_required('home.is_admin')(views.VistaCreateMateria_Actual), name="create_materia_Actual"),

    ##Periodo
    path('tabla_periodo/', permission_required('home.is_admin')(views.VistaTablaPeriodo.as_view()), name="tabla_periodo"),
    path('detalle_periodo/<int:pk>/', permission_required('home.is_admin')(views.VistaDetallePeriodo.as_view()), name="detalle_periodo"),
    path('update_periodo/<int:pk>/', permission_required('home.is_admin')(views.VistaUpdatePeriodo.as_view()), name="update_periodo"),
    path('delete_periodo/<int:pk>/', permission_required('home.is_admin')(views.VistaDeletePeriodo.as_view()), name="delete_periodo"),
    path('create_periodo/', permission_required('home.is_admin')(views.VistaCreatePeriodo), name="create_periodo"),

    #Historial_Materias
    path('tabla_historial_Materias/', permission_required('home.is_admin')(views.VistaTablaHistorial_Materias.as_view()), name="tabla_historial_Materias"),
    path('detalle_historial_Materias/<int:pk>/', permission_required('home.is_admin')(views.VistaDetalleHistorial_Materias.as_view()), name="detalle_historial_Materias"),
    path('update_historial_Materias/<int:pk>/', permission_required('home.is_admin')(views.VistaUpdateHistorial_Materias.as_view()), name="update_historial_Materias"),
    path('delete_historial_Materias/<int:pk>/', permission_required('home.is_admin')(views.VistaDeleteHistorial_Materias.as_view()), name="delete_historial_Materias"),
    path('create_historial_Materias/', permission_required('home.is_admin')(views.VistaCreateHistorial_Materias), name="create_historial_Materias"),


    path('historial_general', views.main , name = 'hg'),


    # Url para inicio y creacion de sesion
    path('login/', auth_views.LoginView.as_view(), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(), name = "logout"),
    path('signup/', views.Signup, name = "signup"),
    
    #Esta vista nos va a redirigir a otra segun el tipo de usuario
    path('casa/', views.Casa, name='casa'),

    #ALUMNOS URLS MODIFICADOS 
    path('home_alumno/', views.Home_Alumno, name='home_alumno'),
    # AVANCE URL DE LOS ALUMNOS 
    path('avance_alumno/',views.Avance_Alumno, name="avance_alumno"),
    # HISTORIAL DESPLEJA UN KARDEX GENERAL  
    path('historial_alumno/', views.Historial_Alumno, name="historial_alumno"),
    # ES UN  MANUEAL DE COMO IMPRIMIR LA PANTALLA 
     path('imprimir_alumno/', views.Imprimir_Alumno, name="imprimir_alumno"), 
    # Boleta_AlumnoView json 
    path('ws/vl/boleta', views.wsBoleta , name ="wsboleta"),
    path('v1/lista_alumno/', views.Lista_Alumno, name = "lista_alumno"),
    path('v1/detail_update_delete_alumno/<int:pk>/', views.detail_update_alumno, name ="detail_update_delete"),
    # path('ws/alumno/boleta/', views.wsAlumno, name = "wsalumno"), ####

    ##Endpoints
    path('v1/list_escuela/', views.List_Escuela, name="list_escuela"),
    #clientes de los endpoints
    path('v1/list_usuario_cliente/', views.wsCliente , name ="list_usuario_cliente"),


    #Nuevos endpoints y apis
    path('v1/detail_materia_actual/<int:pk>/', views.Detail_Materia_Actual, name="detail_materia_actual"),
    path('v1/list_usuario/', views.List_Usuario, name="list_usuario"),
    path('wsMateria_Actual/<int:pk>/', views.wsMateria_Actual, name ="wsmateria_actual"),
    path('ws_Usuario/', views.wsUsuario, name ="wsusuario"),

    ##
    path('grupo_api/', views.Grupo_API.as_view(), name="grupo_api"),
    path('api_alumno/<int:pk>/', views.API_Alumno.as_view(), name="api_alumno"),

    # path('grupo_docente/', views.Grupo_Docente, name="grupo_docente"),
    # path('detalle_alumno/<int:pk>/', views.VistaDetalleAlumno.as_view(), name="detalle_alumno"),

    # path('avance_alumno/',permission_required('home.is_student')(views.Avance_AlumnoView.as_view()), name="avance_alumno"),
    
]