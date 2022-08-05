from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField
from django.urls import reverse 

# Create your models here.

class Alumno(models.Model):
    rut = models.IntegerField()
    dv = models.CharField(max_length=1, blank=True, null=True)
    nombres = models.CharField(max_length=255, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=255, blank=True, null=True)
    apellido_materno = models.CharField(max_length=255, blank=True, null=True)
    nombre_apoderado = models.CharField(max_length=255, blank=True, null=True)
    domicilio_actual = models.CharField(max_length=255, blank=True, null=True)
    Comuna_residencia = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(auto_now=False, blank=True, null=True)
    codigo_etnia = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'



class Establecimiento(models.Model):
    usuario = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    rbd = models.CharField(max_length=6, blank=True, null=True)
    numero_telefonido = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='logo_colegio/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.rbd} {self.nombre}'



class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=255, blank=True, null=True)
    letra = models.CharField(max_length=6, blank=True, null=True)
    año = models.CharField(max_length=4, blank=True, null=True)
    fecha_incorporacion = models.DateField(auto_now=False, blank=True, null=True)
    fecha_retiro = models.DateField(auto_now=False, blank=True, null=True)

    esta_activo = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.alumno} {self.nivel}'
    
    def get_absolute_url(self):
        return reverse('matricula_detail', args=[str(self.id)])


class FuncionarioEstablecimiento(models.Model):
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)

    class Meta:
        db_table = 'funcionario'
        verbose_name = "funcionario"
        verbose_name_plural = "funcionarios"

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido_materno}'
    

    def get_absolute_url(self):
        return reverse('funcionario_detail', args=[str(self.id)])


class Mail(models.Model):
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.email}'
    
    class Meta:
        db_table = 'email'
        ordering = ['-id']
        verbose_name = "email"
        verbose_name_plural = "correos"

    


class CorreosEstablecimiento(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    lista_mails = models.ManyToManyField(Mail)

    def __str__(self) -> str:
        correos = ', '.join(str(v) for v in self.lista_mails.all())
        return f'{self.establecimiento} : {correos}'
    
    class Meta:
        db_table = 'correos_establecimiento'
        ordering = ['-id']
        verbose_name = "correo establecimiento"
        verbose_name_plural = "correos por establecimientos"


class Alerta(models.Model):
    envio_correos_establecimiento = models.ForeignKey(CorreosEstablecimiento, on_delete=models.CASCADE)
    cuerpo_mensaje = models.TextField()

    def __str__(self) -> str:
        return f'{self.envio_correos_establecimiento} : {self.cuerpo_mensaje}'
    
    class Meta:
        db_table = 'alerta'
        ordering = ['-id']
        verbose_name = "alerta rapida"
        verbose_name_plural = "alertas"


class CasoVulneracion(models.Model):
    ONGOING = 'ong'
    NOLEIDO = 'nol'
    FINSH = 'fin'
    STATE_CHOICES = [
        (NOLEIDO, 'No leido'),
        (ONGOING, 'En revisión'),
        (FINSH, 'Finalizado'),
    ]
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=255, choices=STATE_CHOICES, default=NOLEIDO)

    def __str__(self) -> str:
        return f'{self.pk} - {self.fecha_creacion}'

    
    class Meta:
        db_table = 'caso_vulneracion'
        ordering = ['-id']
        verbose_name = "Caso Vulneracion"
        verbose_name_plural = "Casos vulneraciones"
    

    def get_absolute_url(self):
        return reverse('discriminacion_detail', args=[str(self.id)])



class Discriminacion(models.Model):
    ONGOING = 'ong'
    NOLEIDO = 'nol'
    FINSH = 'fin'
    STATE_CHOICES = [
        (NOLEIDO, 'No leido'),
        (ONGOING, 'En revisión'),
        (FINSH, 'Finalizado'),
    ]
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=255, choices=STATE_CHOICES, default=NOLEIDO)

    CARAC_FIS_PER = 'cfp'
    DISC_DIS_INT = 'ddi'
    EMBARAZO_MODERNIDAD = 'em'
    IDENT_GEN = 'ig'
    OPC_RELIG = 'opc'
    ORIEN_SEXUAL = 'os'
    PROBL_SALUD = 'ps'
    MIGRA_RAC = 'mr'
    SDA = 'sda'

    STATE_CHOICES = [
        (CARAC_FIS_PER, 'Características físicas y/o personales'),
        (DISC_DIS_INT, 'Discapacidad física y/o intelectual'),
        (EMBARAZO_MODERNIDAD, 'Embarazo y Maternidad'),
        (IDENT_GEN, 'Identidad de género'),
        (OPC_RELIG, 'Opción religiosa'),
        (ORIEN_SEXUAL, 'Orientación Sexual'),
        (PROBL_SALUD, 'Problemas de Salud'),
        (MIGRA_RAC, 'Ser migrante u origen racial'),
        (SDA, 'Síndrome de déficit atencional'),
    ]

    tipo_discrim = models.CharField(max_length=255, choices=STATE_CHOICES, default=CARAC_FIS_PER)
    victima = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='victima', null=True)
    agresor = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='agresor', null=True)
    detalle = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return f'{self.pk} - {self.detalle}'

    def get_absolute_url(self):
        return reverse('discriminacion_detail', args=[str(self.id)])

    class Meta:
        db_table = 'discriminacion'
        ordering = ['-id']
        verbose_name = "discriminacion"
        verbose_name_plural = "discriminaciones"



class MedidasDiscriminacion(models.Model):
    caso = models.ForeignKey(Discriminacion, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Caso Discriminacion")
    condicionalidad = models.BooleanField()
    devolucion_casa = models.BooleanField()
    expulsion = models.BooleanField()
    suspension_clases = models.BooleanField()
    descripcion_de_medidas = models.CharField(max_length=255)

    class Meta:
        db_table = 'medidas'
        ordering = ['-id']
        verbose_name = "medida discriminacion"
        verbose_name_plural = "medidas discriminacion"

    def __str__(self):
        return f'{self.id} - {self.descripcion_de_medidas}'



class CasoFaltaAConvivencia(models.Model):
    ONGOING = 'ong'
    NOLEIDO = 'nol'
    FINSH = 'fin'
    STATE_CHOICES = [
        (NOLEIDO, 'No leido'),
        (ONGOING, 'En revision'),
        (FINSH, 'Finalizado'),
    ]
    estado = models.CharField(max_length=255, choices=STATE_CHOICES, default=NOLEIDO)

    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, null=True)
    fecha_ingreso = models.DateField()
    informe_detalle = models.TextField(blank=True, null=True)



class Maltrato(models.Model):
    ONGOING = 'ong'
    NOLEIDO = 'nol'
    FINSH = 'fin'
    STATE_CHOICES = [
        (NOLEIDO, 'No leido'),
        (ONGOING, 'En revisión'),
        (FINSH, 'Finalizado'),
    ]
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=255, choices=STATE_CHOICES, default=NOLEIDO)


    TIPO_CHOICES = [
        ('Hacia Estudiantes', (
            ('adulto', 'Adulto a Estudiantes'),
            ('estudiante', 'Estudiante a Estudiante'),
        )
         ),
        ('Hacia Funcionarios', (
            ('alumno_docente', 'Alumno a Docente o Funcionarios'),
            ('apoderado', 'Apoderado a Docente o Funcionarios')

        ),
         )
    ]
    funcionario_agresor = models.ForeignKey(FuncionarioEstablecimiento, on_delete=models.CASCADE,null=True, blank=True, related_name="funcionario_agresor")
    alumno_agresor = models.ForeignKey(Matricula, null=True, blank=True, on_delete=models.CASCADE, related_name="alumno_agresor")

    funcionario_victima = models.ForeignKey(FuncionarioEstablecimiento, on_delete=models.CASCADE, null=True, blank=True, related_name="funcionario_victima")
    victima = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    tipo_maltrato = models.CharField(max_length=255, choices=TIPO_CHOICES, default='estudiante', null=True)
    detalle = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.pk} - {self.fecha_creacion}'

    
    class Meta:
        db_table = 'caso_vulneracion_maltrato'
        ordering = ['-id']
        verbose_name = "Caso Vulneracion Maltrato"
        verbose_name_plural = "Casos vulneraciones Maltrato"
    

    def get_absolute_url(self):
        return reverse('maltrato_detail', args=[str(self.id)])

class ConnotacionSexual(models.Model):
    ONGOING = 'ong'
    NOLEIDO = 'nol'
    FINSH = 'fin'
    STATE_CHOICES = [
        (NOLEIDO, 'No leido'),
        (ONGOING, 'En revisión'),
        (FINSH, 'Finalizado'),
    ]
    
    fecha_creacion = models.DateField(blank=True, null=True)
    
    estado = models.CharField(max_length=255, choices=STATE_CHOICES, default=NOLEIDO)

    AGRESION_SEXUAL = 'agresion'
    NO_AGRESION_SEXUAL = 'noagresion'
    CS_CHOICES = [
        (AGRESION_SEXUAL, 'Agresión sexual'),
        (NO_AGRESION_SEXUAL, 'Delito de connotación sexual que no constituye agresión')
    ]

    tipo_connotacion_sexual = models.CharField(max_length=255, choices=CS_CHOICES, default=AGRESION_SEXUAL)
    detalle = models.CharField(max_length=255, null=True)
    victima = models.ForeignKey(Matricula, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.fecha_creacion} - {self.detalle}'

    def get_absolute_url(self):
        return reverse('connotacion_detail', args=[str(self.id)])


class MedidasConnotacion(models.Model):
    caso = models.ForeignKey(ConnotacionSexual, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Caso Connotacion Sexual")
    condicionalidad = models.BooleanField()
    devolucion_casa = models.BooleanField()
    expulsion = models.BooleanField()
    suspension_clases = models.BooleanField()
    descripcion_de_medidas = models.CharField(max_length=255)

    class Meta:
        db_table = 'medidas_connotacion'
        ordering = ['-id']
        verbose_name = "medida connotacion"
        verbose_name_plural = "medidas connotacion"

    def __str__(self):
        return f'{self.id} - {self.descripcion_de_medidas}'



class MedidasMaltrato(models.Model):
    caso = models.OneToOneField(Maltrato, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Caso Maltrato")
    condicionalidad = models.BooleanField()
    devolucion_casa = models.BooleanField()
    expulsion = models.BooleanField()
    suspension_clases = models.BooleanField()
    descripcion_de_medidas = models.CharField(max_length=255)

    class Meta:
        db_table = 'medidas_maltrato'
        ordering = ['-id']
        verbose_name = "medida maltrato"
        verbose_name_plural = "medidas maltrato"

    def __str__(self):
        return f'{self.id} - {self.descripcion_de_medidas}'

    

class FaltaConvivencia(models.Model):
    REVISION = 'enrev'
    NOLEIDO = 'nol'
    FINSH = 'fin'
    STATE_CHOICES = [
        (NOLEIDO, 'No leido'),
        (REVISION, 'En revision'),
        (FINSH, 'Finalizado'),
    ]
    
    estado = models.CharField(max_length=255, choices=STATE_CHOICES, default=NOLEIDO)
    fecha_ingreso = models.DateField(blank=True, null=True)
    afectado = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    detalle_relato = models.TextField(blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('falta_detail', args=[str(self.id)])


class AccidenteEscolar(models.Model):
    REVISION = 'enrev'
    NOLEIDO = 'nol'
    FINSH = 'fin'
    STATE_CHOICES = [
        (NOLEIDO, 'No leido'),
        (REVISION, 'En revision'),
        (FINSH, 'Finalizado'),
    ]
    
    estado = models.CharField(max_length=255, choices=STATE_CHOICES, default=NOLEIDO)
    accidentado = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(blank=True, null=True)

    malestar_fisico = models.CharField(max_length=255, blank=True, null=True)
    nombre_familiar_contacto = models.CharField(max_length=255, blank=True, null=True)
    instruccion_familiar = models.CharField(max_length=255, blank=True, null=True)

    consecuencias_medicas = models.CharField(max_length=255, blank=True, null=True)

    # descripcion_breve = models.TextField(blank=True, null=True)
    detalle_relato = models.TextField(blank=True, null=True)

    testigo_uno = models.CharField(max_length=255, blank=True, null=True)
    testigo_dos = models.CharField(max_length=255, blank=True, null=True)

    archivo_declaracion_individual = models.FileField(upload_to='declaracion_individual/', blank=True, null=True)

    llama_apoderado = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'caso_accidente'
        verbose_name = "caso accidente"
        verbose_name_plural = "casos accidentes"

    def __str__(self) -> str:
        return f'{self.accidentado} {self.detalle_relato} {self.estado}'

    def get_absolute_url(self):
        return reverse('detail_accidente', args=[str(self.id)])

        

class DerivacionOTP(models.Model):
    pass


class DificultadConstitucionConsejo(models.Model):
    REVISION = 'enrev'
    NOLEIDO = 'nol'
    FINSH = 'fin'
    STATE_CHOICES = [
        (NOLEIDO, 'No leido'),
        (REVISION, 'En revision'),
        (FINSH, 'Finalizado'),
    ]

    CENTRO_ALUMNOS = 'cc_aa'
    CENTRO_PPAA = 'cc_ppaa'
    CONSEJO = 'consejo'
    TIPO_CHOICES = [
        (CENTRO_ALUMNOS, 'Centro de Alumnos(as)'),
        (CENTRO_PPAA, 'Centro de padres y apoderados'),
        (CONSEJO, 'Consejo de Curso o Comité de buena convivencia')
    ]

    estado = models.CharField(max_length=255, choices=STATE_CHOICES, default=NOLEIDO)
    tipo_consejos = models.CharField(max_length=255, choices=TIPO_CHOICES, default=NOLEIDO)
    funcionario_afectado = models.ForeignKey(FuncionarioEstablecimiento, on_delete=models.CASCADE)
    fecha = models.DateField()
    detalle = models.CharField(max_length=255)

    class Meta:
        db_table = 'dificultad_consejo'
        verbose_name = "Dificultad en consejo"
        verbose_name_plural = "Dificultades en consejos"

    def __str__(self) -> str:
        return f'{self.funcionario_afectado} {self.detalle} {self.estado}'
    
    def get_absolute_url(self):
        return reverse('detail_dificultad', args=[str(self.id)])


class VulneracionDerechosFuncionarios(models.Model):
    REVISION = 'enrev'
    NOLEIDO = 'nol'
    FINSH = 'fin'
    STATE_CHOICES = [
        (NOLEIDO, 'No leido'),
        (REVISION, 'En revision'),
        (FINSH, 'Finalizado'),
    ]

    INCUMPLIMIENTO = 'inc'
    NOPAGO_REMUNERACION = 'nopr'
    LIBERTAD_CONCIENCIA = ''
    LIBERTAD_EXPRESION = ''
    LIBERTAD_CONCIENCIA = ''
    TIPO_CHOICES = [
        (INCUMPLIMIENTO, 'Incumplimiento de obligaciones laborales'),
        (NOPAGO_REMUNERACION, 'No pago de remuneraciones'),
    ]


    estado = models.CharField(max_length=255, choices=STATE_CHOICES, default=NOLEIDO)
    tipo_vulneracion = models.CharField(max_length=255, choices=TIPO_CHOICES, default=INCUMPLIMIENTO)
    funcionario_afectado = models.ForeignKey(FuncionarioEstablecimiento, on_delete=models.CASCADE)
    fecha = models.DateField()
    detalle = models.CharField(max_length=255)

    class Meta:
        db_table = 'vulneracion_derechos_funcionarios'
        verbose_name = "Vulneracion de derechos a funcionarios"
        verbose_name_plural = "Vulneraciones de derechos a funcionarios"

    def __str__(self) -> str:
        return f'{self.funcionario_afectado} {self.detalle} {self.estado}'
    
    def get_absolute_url(self):
        return reverse('detail_vulneracion_funcionario', args=[str(self.id)])



class VulneracionGarantiasConstitucionales(models.Model):
    pass