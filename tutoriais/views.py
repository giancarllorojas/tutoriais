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
        tutorial_obj = Tutorial.objects.get(pk=tutorial_id)
    except Tutorial.DoesNotExist:
        raise Http404("Tutorial não existe")

    try:
        artigo_obj = Artigo.objects.get(pk=artigo_id)
    except:
        artigo_obj = Artigo.objects.get(tutorial=tutorial_obj, posicao=0)

    try:
        anterior = Artigo.objects.get(tutorial=tutorial_obj, posicao=artigo_obj.posicao-1)
    except:
        anterior = None

    try:
        proximo = Artigo.objects.get(tutorial=tutorial_obj, posicao=artigo_obj.posicao+1)
    except:
        proximo = None

    template = loader.get_template('tutoriais/tutorial.html')
    contexto = {
        'tutorial': tutorial_obj,
        'artigo': artigo_obj,
        'artigos': Artigo.objects.filter(tutorial=tutorial_obj),
        'secoes': Secao.objects.filter(tutorial=tutorial_obj).order_by('posicao'),
        'anterior': anterior,
        'proximo': proximo
    }

    return HttpResponse(template.render(contexto, request))

def ver_tutorial(request, tutorial_id):
    return ver_artigo(request, tutorial_id, -1)