from django.shortcuts import render

# Create your views here.
import os

import pdfkit
from django.http import HttpResponse
from django.template import loader

def html_to_pdf_view(request):
    html = loader.render_to_string('invoice.html') # rendering the html page to string
    print(html)

    options = {
        'page-size': 'letter',
        'margin-top': '0.55in',
        'margin-right': '0.55in',
        'margin-bottom': '0.55in',
        'margin-left': '0.55in',

    }

    output= pdfkit.from_string(html, output_path=False,options=options) #here pdf is generated.Output path=false is used to store file in variable.
    response = HttpResponse(content_type="application/pdf") # # Create the HttpResponse object with the appropriate PDF headers.
    response.write(output)
    return response