from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    '''now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
'''
    #return HttpResponse(html)
    return render(request, 'core/home.html')
   

def cadastroaluno(request):
    return render(request, 'core/cadastroaluno.html')

def cadastroservidor(request):
    return render(request, 'core/cadastroservidor.html')

def presencasefaltas(request):
    return render(request, 'core/presencasefaltas.html')

def justificarfaltas(request):
    return render(request, 'core/justificarfaltas.html')

def declaracaoestudantil(request):
    return render(request, 'core/declaracaoestudantil.html')

def notificacoes(request):
    return render(request, 'core/notificacoes.html')
