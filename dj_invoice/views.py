import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import smart_str
from django.conf import settings

from PyPDF2 import PdfFileWriter, PdfFileReader

def create_invoice(request):
    """ creates an invoice given query parameters """
    
    templates_dir = getattr(settings, 'DJ_INVOICE_DIRECTORY', '../templates')

    output = PdfFileWriter()
    input_pdf = PdfFileReader(open(os.path.join(templates_dir, 'example.pdf'), "rb"))
    print input_pdf

    #output = PdfFileWriter()
    #input1 = PdfFileReader(open("document1.pdf", "rb"))
    
    return HttpResponse("create_invoice")
    
def list_invoices(request):
    """ list invoices given query parameters """
    
    return HttpResponse("list_invoices")