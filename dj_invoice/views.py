import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import smart_str
from django.conf import settings

from PyPDF2 import PdfFileWriter, PdfFileReader

def write_to_pdf(input_pdf, data=[]):
    """ write data to the pdf """

def create_invoice(request):
    """ creates an invoice given query parameters """
    
    templates_dir = getattr(settings, 'DJ_INVOICE_DIRECTORY', 
        os.path.join(settings.BASE_DIR, 'templates'))
    invoice_pdf_name = getattr(settings, 'DJ_INVOICE_PDF_NAME', 'example.pdf')

    output = PdfFileWriter()
    input_pdf = PdfFileReader(open(os.path.join(templates_dir, invoice_pdf_name), "rb"))
    
    return HttpResponse("create_invoice")
    
def list_invoices(request):
    """ list invoices given query parameters """
    
    return HttpResponse("list_invoices")