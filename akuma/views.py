from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "pages/index.html"
    extra_context = {
        'titulo': "Landing Page"
        } 

class Contacto(TemplateView):
    template_name = "pages/contacto.html"
    extra_context = {
        'titulo': "Contacto Page"
        } 

class Somos(TemplateView):
    template_name = "pages/somos.html"
    extra_context = {
        'titulo': "Somos Page"
        } 

class Ventas(TemplateView):
    template_name = "pages/ventas.html"
    extra_context = {
        'titulo': "Ventas Page"
        } 