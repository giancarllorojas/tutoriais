from django.http import HttpResponse, Http404
from django.template import loader
from .models import *


def index(request):
    return HttpResponse("Hello, world tutorials")

def lista_tutoriais(request):
    tutoriais = Tutorial.objects.order_by('-datatempo')
    template = loader.get_template('tutoriais/lista.html')
    contexto = {
        'tutoriais': tutoriais
    }
    return HttpResponse(template.render(contexto, request))

def lista_tutoriais_categoria(request, categoria_id):
    return HttpResponse("hi cat")

def ver_artigo(request, tutorial_id, artigo_id):
    try:
        tutorial_obj = Tutorial.objects.get(pk="programacao_c")
    except Tutorial.DoesNotExist:
        raise Http404("Tutorial não existe")

    try:
        artigo_obj = Artigo.objects.get(tutorial=tutorial_obj, pk=artigo_id)
    except:
        raise Http404("Artigo não existe")

    return HttpResponse(artigo_obj)

def ver_tutorial(request, tutorial_id):
    return HttpResponse("t: :" + tutorial_id)