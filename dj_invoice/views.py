import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import smart_str
from django.conf import settings

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import StringIO

def write_to_pdf(input_pdf, data=[]):
    """ write data to the pdf """
    # op = PdfFileWriter()
    # op.addBlankPage(200,200)
    # ops = file("document-output.pdf", "wb")
    # op.write(ops)
    # ops.close()
    
    can.setFont("Helvetica", 9)
    packet = StringIO.StringIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString( 200, 540,  'HELLO WORLD')
    can.save()

    packet.seek(0)
    output_pdf = PdfFileReader(packet)
    default_pdf = PdfFileReader(file("document-output.pdf", "wb"))
    output = PdfFileWriter()
    
    output_stream = file(self.output_path, "wb")
    output.write(output_stream)
    output_stream.close()
    
    
def create_pdf_from_scratch(data=[]):
    """ write data to the pdf """
    print('---- create_pdf_from_scratch')
    op = PdfFileWriter()
    op.addBlankPage(200,200)  
    ops = file("document-output.pdf", "wb")  
    op.write(ops)  
    ops.close()

def create_invoice(request):
    """ creates an invoice given query parameters """
    
    templates_dir = getattr(settings, 'DJ_INVOICE_DIRECTORY', 
        os.path.join(settings.BASE_DIR, 'templates'))
    invoice_pdf_name = getattr(settings, 'DJ_INVOICE_PDF_NAME', 'example.pdf')

    generate = request.REQUEST.get("generate")
    if generate:
        output = PdfFileWriter()
        input_pdf = PdfFileReader(open(os.path.join(templates_dir, invoice_pdf_name), "rb"))
    else:
        create_pdf_from_scratch()
    
    return HttpResponse("create_invoice")
    
def list_invoices(request):
    """ list invoices given query parameters """
    
    return HttpResponse("list_invoices")