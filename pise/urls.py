from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='index'),
    path('accounts/login/', views.UserLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    #Establecimiento
    path('ajustes/<int:pk>', views.EstablecimientoUsuarioDetailView.as_view(),name='detail'),
    path('ajustes/<int:pk>/actualizar',views.EstablecimientoUsuarioUpdateView.as_view(),name='update'),
    #Alumnos
    path('matriculas/', views.MatriculaEstablecimientoListView.as_view(), name='matriculas'),
    path('matricula/<int:pk>', views.MatriculaEstablecimientoDetailView.as_view(), name='matricula_detail'),
    path('matricula/<int:pk>/actualizar',views.MatriculaEstablecimientoUpdateView.as_view(), name='matricula_edit' ),
    path('matriculas/crear', views.CargarNominaMatriculas, name='matriculas_create'),
    path('matriculas/inscribir', views.MatriculaEstablecimientoCreateView.as_view(), name='matriculas_add'),
    #Funcionarios
    path('funcionarios/', views.FuncionarioEstablecimientoListView.as_view(), name='funcionarios'),
    path('funcionario/<int:pk>', views.FuncionarioEstablecimientoDetailView.as_view(), name='funcionario_detail'),
    path('funcionario/<int:pk>/actualizar',views.FuncionarioEstablecimientoUpdateView.as_view(), name='funcionario_edit' ),
    path('funcionario/crear', views.FuncionarioEstablecimientoCreateView.as_view(), name='funcionario_add'),
    #CASOS
    path('caso/', views.CasoCreateView.as_view(), name='create_caso'),
    path('caso/<int:pk>/update', views.CasoUpdateView.as_view(), name='update_caso'),
    # CRUD DISCRIMINACION

    path('casos_discriminacion', views.DiscriminacionListView.as_view(), name='discriminacion_list'),
    path('caso_discriminacion/crear', views.DiscriminacionCreateView.as_view(), name='discriminacion_add'),
    path('discriminacion/<int:pk>', views.DiscriminacionDetailView.as_view(), name='discriminacion_detail'),
    # path('discriminacion/crear', views.DiscriminacionCreateView.as_view(), name='discriminacion_add'),
    # MEDIDAS DISCRIMINACION
    path('discriminacion/<int:pk>/medidas', views.medidas_discriminacion_view, name='discriminacion_medidas'),
    path('discriminacion/<int:pk>/medidas/actualizar', views.actualizar_medidas_discriminacion, name='actualizar_discriminacion_medidas'),
    path('caso_discriminacion/<int:pk>/update', views.DiscriminacionUpdateView.as_view(), name='discriminacion_update'),

    # CRUD Maltrato
    #path('caso_maltrato/', views.CasoMaltratoCreateView.as_view(), name='create_caso_maltrato'),
    path('caso_maltrato/crear', views.MaltratoCreateView.as_view(), name='maltrato_add'),
    path('caso_maltrato/crear/menor_a_menor', views.MaltratoAlumnoToAlumnoCreateView.as_view(), name='maltrato_alumnotoalumno_add'),
    path('caso_maltrato/crear/adulto_a_menor', views.MaltratoFuncionarioToAlumnoCreateView.as_view(), name='maltrato_funcionariotoalumno_add'),
    path('caso_maltrato/crear/adulto_a_adulto', views.MaltratoAdultoToAdultoCreateView.as_view(), name='maltrato_adultotoadulto_add'),
    path('caso_maltrato/crear/funcionario_a_alumno', views.MaltratoFuncionarioToAlumnoCreateView.as_view(), name='maltrato_funcionariotoalumno_add'),

    path('caso_maltrato/<int:pk>', views.MaltratoDetailView.as_view(), name='maltrato_detail'),
    path('casos_maltrato/', views.MaltratoListView.as_view(), name='maltrato_list'),
    path('caso_maltrato/<int:pk>/actualizar', views.MaltratoUpdateView.as_view(), name='maltrato_update'),
    #path('caso_maltrato/<int:pk>/medidas', views.MedidasMaltratoView.as_view(), name='maltrato_medidas'),
    path('caso_maltrato/<int:pk>/medidas/crear', views.medidas_maltrato_view, name='add_maltrato_medidas'),
    path('caso_maltrato/<int:pk>/medidas/update', views.actualizar_medidas_maltratos, name='actualizar_maltrato_medidas'),


    # CRUD Connotacion
    path('caso_connotacion/crear', views.FullConnotacionSexualCreateView.as_view(), name='create_caso_connotacion'),
    path('casos_connotacion/', views.ConnotacionSexualListView.as_view(), name='connotacion_list'),
    #path('caso_connotacion/<int:pk>/connotacion/crear/', views.ConnotacionSexualCreateView.as_view(), name='connotacion_add'),
    path('caso_connotacion/<int:pk>', views.ConnotacionSexualDetailView.as_view(), name='connotacion_detail'),
    path('caso_connotacion/<int:pk>/update', views.ConnotacionSexualUpdateView.as_view(), name='connotacion_update'),

    #CRUD ACCIDENTE_ESCOLAR

    path('caso_accidente/create', views.AccidenteEscolarCreateView.as_view(), name='add_accidente'),
    path('caso_accidente/<int:pk>', views.AccidenteEscolarDetailView.as_view(), name='detail_accidente'),
    path('caso_accidente/<int:pk>/actualizar', views.AccidenteEscolarUpdateView.as_view(), name='update_accidente'),
    path('caso_accidente/<int:pk>/actualizar_estado', views.AccidenteEscolarEstadoUpdateView.as_view(), name='update_estado_accidente'),
    path('casos_accidente/', views.AccidenteEscolarListView.as_view(), name='list_accidente'),

    #CRUD DIFICULTAD CONSEJOS
    path('caso_consejo/create', views.DificultadConstitucionCreateView.as_view(), name='add_dificultad'),
    path('caso_consejo/<int:pk>', views.DificultadConstitucionDetailView.as_view(), name='detail_dificultad'),
    path('caso_consejos/', views.DificultadConstitucionListView.as_view(), name='list_dificultad'),
    path('caso_consejo/<int:pk>/actualizar_estado', views.DificultadConsejoEstadoUpdateView.as_view(), name='update_status_dificultad'),

    #CRUD VULNERACION DERECHOS FUNCIONARIOS
    path('caso_vulneracion_funcionarios/create', views.VulneracionDerechosFuncionariosCreateView.as_view(), name='add_vulneracion_funcionario'),
    path('casos_vulneraciones_funcionarios/', views.VulneracionDerechosFuncionariosListView.as_view(), name='list_vulneracion_funcionario'),
    path('caso_vulneracion_funcionarios/<int:pk>', views.VulneracionDerechosFuncionariosDetailView.as_view(), name='detail_vulneracion_funcionario'),
    path('caso_vulneracion_funcionarios/<int:pk>/actualizar_estado', views.VulneracionFuncionariosEstadoUpdateView.as_view(), name='update_status_vulneracion_funcionario'),

    #descarga_archivo_accidente_escolar
    path('descargar_dec/', views.descarga_archivo_accidente_escolar, name='download_dec'),
    path('reportes/', views.ReportesView.as_view(), name='reportes'),

    #Creación de PDF
    path('reporte_maltrato/<int:pk>', views.report_vulneracion, name='reporte-vulneracion'),
    path('report_discriminacion/<int:pk>', views.report_discriminacion, name='reporte-discrim'),
    path('report_connotacion/<int:pk>', views.report_connotacionsexual, name='reporte-connotacion'),
    path('report_dificultad_consejo_escolar/<int:pk>', views.report_dificultad_consejo_escolar, name='reporte-dificultad'),
    path('report_vulneracion_derechos_funcionarios/<int:pk>', views.report_vulneracion_derechos_funcionario, name='reporte-vulneracion-funcionarios'),

    #CRUD Alumno
    #path('matriculas/Agregar', views.MatriculaCreateView.as_view(), name='add_alumn'),


] 