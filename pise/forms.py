from dataclasses import fields
from faulthandler import disable
from pyexpat import model
from django import forms
from django.forms import widgets
from . import models
from django.core.validators import FileExtensionValidator



class AlertaForm(forms.ModelForm):
    class Meta:
        model = models.Alerta
        fields = ['cuerpo_mensaje']
        widgets = {
            'cuerpo_mensaje': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Cuerpo del Mensaje...', 'required': True}
            )
        }

class CasoVulneracion(forms.ModelForm):
    class Meta:
        model = models.CasoVulneracion
        fields = ['fecha_creacion']

class DiscriminacionCreateForm(forms.ModelForm):
    class Meta:
        model = models.Discriminacion
        fields = ['tipo_discrim',  'fecha_creacion', 'victima', 'agresor', 'detalle']
        widgets = {
            'detalle': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Relato de lo sucedido', 'required': True}
            ),
            'victima': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'agresor': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'tipo_discrim': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'fecha_creacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }

    # def __init__(self, *args, **kwargs):
    #     caso = kwargs.pop('caso', '')
    #     super(DiscriminacionCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['fecha_creaciones']=forms.DateField()

class MedidasDiscriminacion(forms.ModelForm):
    class Meta:
        model = models.MedidasDiscriminacion
        fields = ['condicionalidad', 'devolucion_casa', 'expulsion', 'suspension_clases', 'descripcion_de_medidas']
        widgets = {
            'descripcion_de_medidas': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Detalle de las medidas adoptadas', 'required': True}
            ),
        }


class MaltratoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Maltrato
        fields = ['fecha_creacion', 'tipo_maltrato', 'victima','detalle', 'funcionario_agresor']
        widgets = {
            'detalle': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Relato de lo sucedido', 'required': True}
            ),
            'victima': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'funcionario_agresor': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'tipo_maltrato': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'fecha_creacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }

class MaltratoAlumnoToAlumnoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Maltrato
        fields = ['fecha_creacion', 'tipo_maltrato', 'victima','detalle', 'alumno_agresor']
        widgets = {
            'detalle': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Relato de lo sucedido', 'required': True}
            ),
            'victima': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'alumno_agresor': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'tipo_maltrato': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'fecha_creacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }


class MaltratoFuncionarioToAlumnoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Maltrato
        fields = ['fecha_creacion', 'victima','detalle', 'funcionario_agresor']
        widgets = {
            'detalle': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Relato de lo sucedido', 'required': True}
            ),
            'victima': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'funcionario_agresor': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'fecha_creacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }


class ConnotacionSexualCreateForm(forms.ModelForm):
    class Meta:
        model = models.ConnotacionSexual
        fields = ['fecha_creacion','tipo_connotacion_sexual', 'detalle', 'victima']
        widgets = {
            'detalle': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Relato de lo sucedido', 'required': True}
            ),
            'victima': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'tipo_connotacion_sexual': forms.Select(
                attrs={'class': 'form-control',}
            ),
            'fecha_creacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }


class EstadoConnotacionSexualCreateForm(forms.ModelForm):
    class Meta:
        model = models.ConnotacionSexual
        fields = ['estado']
        widgets = {
            'estado': forms.Select(
                attrs={'class': 'form-control',}
            )
        }

class EstadoMaltratoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Maltrato
        fields = ['estado']
        widgets = {
            'estado': forms.Select(
                attrs={'class': 'form-control',}
            )
        }


class EstadoDiscriminacionCreateForm(forms.ModelForm):
    class Meta:
        model = models.Discriminacion
        fields = ['estado']
        widgets = {
            'estado': forms.Select(
                attrs={'class': 'form-control',}
            )
        }


class MedidasMaltratoForm(forms.ModelForm):
    class Meta:
        model = models.MedidasMaltrato
        fields = ['condicionalidad', 'devolucion_casa', 'expulsion', 'suspension_clases', 'descripcion_de_medidas']
        widgets = {
            'descripcion_de_medidas': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Detalle de las medidas adoptadas', 'required': True}
            ),
        }


class AccidenteEscolarActualizarEstadoForm(forms.ModelForm):
    class Meta:
        model = models.AccidenteEscolar
        fields = ['estado']
        widgets = {
            'estado': forms.Select(
                attrs={'class': 'form-control',}
            )
        }


class AccidenteEscolarForm(forms.ModelForm):
    class Meta:
        model = models.AccidenteEscolar
        exclude =('estado',)
        # ['matricula_accidente', 'fecha_ingreso', 'malestar_fisico', 
        #     'nombre_familiar_contacto', 'instruccion_familiar','consecuencias_medicas', 'detalle_relato',
        #     'testigo_uno', 'testigo_dos', 'archivo_declaracion_individual']
        widgets = {
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'tipo_accidente': forms.Select(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'type': 'date'}),
            'malestar_fisico': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Malestar Físico', 'required': True}),
            'nombre_familiar_contacto': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Familiar Contacto', 'required': True}),
            'instruccion_familiar': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Instrucción Familiar', 'required': True}),
            'consecuencias_medicas': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Consecuencias Médicas', 'required': True}),
            'descripcion_breve': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Consecuencias Médicas', 'required': True}),
            'detalle_relato': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Detalle del accidente', 'required': True}),
            'testigo_uno': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Testigo Uno', 'required': True}),
            'testigo_dos': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Testigo Dos', 'required': True}),
            'archivo_declaracion_individual': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
            'llama_apoderado': forms.CheckboxInput(
                attrs={'class': 'form-check-input ml-1'}
            )

        }


class DificultadConstitucionConsejoForm(forms.ModelForm):
    class Meta:
        model = models.DificultadConstitucionConsejo
        fields = ['tipo_consejos', 'funcionario_afectado', 'fecha', 'detalle']
        widgets = {
            'tipo_consejos': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'funcionario_afectado': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'fecha': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'detalle': forms.Textarea(
                attrs={'class': 'form-control'}
            ),

        }
    
    def __init__(self, *args, **kwargs):
        super(DificultadConstitucionConsejoForm, self).__init__(*args, **kwargs)
        self.fields['funcionario_afectado'].empty_label = "Seleccione funcionario"




class VulneracionDerechosFuncionariosForm(forms.ModelForm):
    class Meta:
        model = models.VulneracionDerechosFuncionarios
        fields = ['tipo_vulneracion', 'funcionario_afectado', 'fecha', 'detalle']
        widgets = {
            'tipo_vulneracion': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'funcionario_afectado': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'fecha': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'detalle': forms.Textarea(
                attrs={'class': 'form-control'}
            ),

        }


class EstadoVulneracionFuncionariosUpdateForm(forms.ModelForm):
    class Meta:
        model = models.VulneracionDerechosFuncionarios
        fields = ['estado']
        widgets = {
            'estado': forms.Select(
                attrs={'class': 'form-control',}
            )
        }


class EstadoDificultadConsejoUpdateForm(forms.ModelForm):
    class Meta:
        model = models.DificultadConstitucionConsejo
        fields = ['estado']
        widgets = {
            'estado': forms.Select(
                attrs={'class': 'form-control',}
            )
        }

class EstablecimientoUsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Establecimiento
        fields = ('nombre','telefono','direccion', 'logo','reglamento_interno')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control',}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control',}),
            'direccion': forms.TextInput(attrs={'class': 'form-control',}),
            'logo': forms.FileInput(attrs={'class': 'form-control',}),
            'reglamento_interno': forms.FileInput(attrs={'class': 'form-control',})
        }

class MatriculaEstablecimientoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Matricula
        exclude = ['año','establecimiento','nombre_apoderado','esta_activo']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control',}),
            'dv': forms.TextInput(attrs={'class': 'col col-md-1',}),
            'genero': forms.TextInput(attrs={'class': 'col col-md-1',}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres', 'required': True,}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Paterno', 'required': True}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Materno', 'required': True}),
            'domicilio_actual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Domicilio', 'required': True}),
            'Comuna_residencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comuna', 'required': True}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'required': True}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono', 'required': False}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular', 'required': False}),
            'fecha_nacimiento': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'type': 'date'}),
            'codigo_etnia': forms.NumberInput(attrs={'class':'form-control','type':'number'}),
            #matricula
            'nivel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion Grado', 'required': True,}),
            'letra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Letra Curso', 'required': True}),
            'fecha_incorporacion': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_retiro': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'type': 'date'}),
        }
class MatriculaEstablecimientoEditForm(forms.ModelForm):
    class Meta:
        model = models.Matricula
        exclude = ['año','establecimiento','rut','dv','nombres','apellido_paterno','apellido_materno','codigo_etnia','fecha_nacimiento','fecha_incorporacion','fecha_retiro']
        widgets = {
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'nombre_apoderado': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre Apoderado', 'required': True}),
            'domicilio_actual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Domicilio', 'required': True}),
            'Comuna_residencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comuna', 'required': True}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'required': True}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono', 'required': False}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular', 'required': False}),
            #matricula
            'nivel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion Grado', 'required': True,}),
            'letra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Letra Curso', 'required': True})
        }