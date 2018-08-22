from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect



def index_adopcion(request):
	return HttpResponse("soy la pagina principal de la app adopcion")

