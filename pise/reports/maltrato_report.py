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


class ReporteMaltrato():

    def __init__(self, caso:models.Maltrato=None, request=None ) -> None:
        self.caso = caso
        self.request = request

    
    def create_pdf(self):

        if self.caso.estado == 'nol':
            return render(self.request, 'errores/caso_noleido.html', {})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="maltrato_nombre"'

        pdf = SimpleDocTemplate(response, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=50, bottomMargin=0)
        styles = getSampleStyleSheet()
        elemWidth = 500
        titleTable = Table([
            [Paragraph("<para align=center>Caso Maltrato Escolar</para>", styles['Heading1'])]
        ], elemWidth)

        rut = f'{self.caso.victima.alumno.rut}-{self.caso.victima.alumno.dv}'
        edad = relativedelta(datetime.now(), self.caso.victima.alumno.fecha_nacimiento).years

        alumno_data = Table([
            ["Nombre: ", self.caso.victima.alumno, "Rut: " , rut],
            ["Fecha Nacimiento: ", self.caso.victima.alumno.fecha_nacimiento, "Edad: ", edad],
            ["Direccion: ", self.caso.victima.alumno.domicilio_actual],
            ["Apoderado: ", self.caso.victima.alumno.nombre_apoderado],
            
        ], [100, 150, 50, 150])

        infoColegio = Table([
            [Paragraph("<para align=center>Información del Colegio</para>", styles['Heading2'])]
        ], elemWidth)

        datos_establecimiento = Table([
            ["Establecimiento: ", self.caso.victima.establecimiento.nombre],
            ["Direccion Establecimiento: ", self.caso.victima.establecimiento.direccion],
            ["Número Contacto: ", self.caso.victima.establecimiento.numero_telefonido],
        ], 150)

        infoCaso = Table([
            [Paragraph("<para align=center>Información del caso</para>", styles['Heading3'])]
        ], elemWidth)

        tipo_caso = Table([
            ["Tipo de Caso: ", self.caso.get_tipo_maltrato_display()],
            ["Fecha del Caso: ", self.caso.fecha_creacion.strftime('%d/%m/%Y')],
        ], 100)

        detalle_caso = Table([
            ['Detalle: ', ]
        ], [50, 150])
        
        elementTable = Table([
            [titleTable],
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

        pdf.title = "Caso Maltrato Escolar"
        pdf.build(Story)
        

        return response

    


