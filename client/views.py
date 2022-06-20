from django.shortcuts import render
from django.http import HttpResponse
from api.models import Sondage
# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def question(request):
	return render(request, 'question.html', {"sondage": Sondage.objects.all()})