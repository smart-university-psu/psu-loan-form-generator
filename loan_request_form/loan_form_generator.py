import io
import PyPDF2
from reportlab.lib import pagesizes
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def create(data: dict):
    pdfmetrics.registerFont(TTFont('Sarabun', 'loan_request_form/SRB.ttf'))
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=pagesizes.A4)
    c.setFont("Sarabun", 10)
    c.translate(mm, mm)

    c.drawString(x=97 * mm, y=267 * mm, text=data["type"])
    c.drawString(x=127 * mm, y=252 * mm, text=data["date"])
    c.drawString(x=150 * mm, y=252 * mm, text=data["month"])
    c.drawString(x=178 * mm, y=252 * mm, text=data["year"])
    c.drawString(x=124 * mm, y=242 * mm, text=data["campus"])
    c.drawString(x=36 * mm, y=232 * mm, text=data["fullname"])
    c.drawString(x=110 * mm, y=232 * mm, text=data["position"])
    c.drawString(x=170 * mm, y=232 * mm, text=data["salary_id"])
    c.drawString(x=45 * mm, y=219 * mm, text=data["org"])
    c.drawString(x=112 * mm, y=219 * mm, text=data["internel_tel"])
    c.drawString(x=150 * mm, y=219 * mm, text=data["mobile"])
    c.drawString(x=70 * mm, y=213 * mm, text=data["salary"])
    c.drawString(x=120 * mm, y=213 * mm, text=data["net_salary"])
    c.drawString(x=80 * mm, y=201 * mm, text=data["loan_amount"])
    c.drawString(x=105 * mm, y=201 * mm, text=data["loan_amount_desc"])
    c.drawString(x=98 * mm, y=162 * mm, text=data["fullname"])

    c.save()
    packet.seek(0)
    new_pdf = PyPDF2.PdfFileReader(packet)
    template_pdf = PyPDF2.PdfFileReader(open("loan_request_form/loan_request_form_template.pdf", "rb"))
    output = PyPDF2.PdfFileWriter()
    page = template_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    output_stream = open("output/loan_request_form.pdf", "wb")
    output.write(output_stream)
    output_stream.close()
