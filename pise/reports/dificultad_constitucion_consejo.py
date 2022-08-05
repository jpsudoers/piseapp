from datetime import datetime
import io
# ReportLab
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table

from .. import models

#Django modules
from django.http import HttpResponse
from django.shortcuts import render

from dateutil.relativedelta import relativedelta

from .. import models

class ReportDificultadConstitucionConsejo():

    def __init__(self, caso:models.DificultadConstitucionConsejo=None, request=None ) -> None:
        self.caso = caso
        self.request = request

    
    def create_pdf(self):

        # if self.caso.estado == 'nol':
        #     return render(self.request, 'errores/caso_noleido.html', {})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="dificultad_constitucionconsejo_nombre"'

        pdf = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=50, bottomMargin=0)
        styles = getSampleStyleSheet()
        elemWidth = 500
        titleTable = Table([
            [Paragraph("<para align=center>Caso Dificultad en Constitución de Consejo Escolar</para>", styles['Heading1'])],
            [Spacer(0,20)]
        ], elemWidth)

        rut = f'{self.caso.funcionario_afectado.rut}-{self.caso.funcionario_afectado.dv}'
        edad = relativedelta(datetime.now(), self.caso.funcionario_afectado.fecha_nacimiento).years

        infoAlumno = Table([
            [Paragraph("<para align=center>Información del Funcionario</para>", styles['Heading2'])]
        ], elemWidth)

        alumno_data = Table([
            ["Nombre: ", f'{self.caso.funcionario_afectado.nombre} {self.caso.funcionario_afectado.apellido_paterno}',"Rut: " , rut],
            ["Fecha Nacimiento: ", self.caso.funcionario_afectado.fecha_nacimiento, "Edad: ", edad],
            ["Direccion: ", self.caso.funcionario_afectado.direccion],
            ["Cargo: ", self.caso.funcionario_afectado.cargo],
            [Spacer(0,20)]
            
        ], [100, 150, 50, 150])

        infoColegio = Table([
            [Paragraph("<para align=center>Información del Colegio</para>", styles['Heading2'])]
        ], elemWidth)

        datos_establecimiento = Table([
            ["Establecimiento: ", self.caso.funcionario_afectado.establecimiento.nombre],
            ["Direccion Establecimiento: ", self.caso.funcionario_afectado.establecimiento.direccion],
            ["Número Contacto: ", self.caso.funcionario_afectado.establecimiento.numero_telefonido],
            [Spacer(0,20)]
        ], 150)

        infoCaso = Table([
            [Paragraph("<para align=center>Información del Caso </para>", styles['Heading2'])]
        ], elemWidth)

        tipo_caso = Table([
            ["Tipo de Caso: ", self.caso.get_tipo_consejos_display()],
            ["Fecha del Caso: ", self.caso.fecha.strftime('%d/%m/%Y')],
        ], 100)

        detalle_caso = Table([
            ['Detalle: ', ]
        ], [50, 150])
        
        elementTable = Table([
            [titleTable],
            [infoAlumno],
            [alumno_data],
            [infoColegio],
            [datos_establecimiento],
            [infoCaso],
            [tipo_caso],
            [detalle_caso]
        ])

        Story = []
        Story.append(elementTable)
        Story.append(Paragraph(self.caso.detalle))
        

        # ptext = '<para align=center>Caso Maltrato Escolar</para>'
        # Story.append(Paragraph(ptext, styles['Heading1']))

        # ptext = "Victima: %s" % str(self.caso.victima.alumno)
        # Story.append(Paragraph(ptext))

        # ptext = "Fecha del Caso: %s" % str(self.caso.fecha_creacion)
        # Story.append(Paragraph(ptext))

        # ptext = "Detalle del Caso: %s" % str(self.caso.detalle)
        # Story.append(Paragraph(ptext))

        # ptext = "Tipo Maltrato: %s" % str(self.caso.get_tipo_maltrato_display())
        # Story.append(Paragraph(ptext))

        pdf.title = "Caso Dificultad en Consejo Escolar"
        pdf.build(Story)
        

        return response
