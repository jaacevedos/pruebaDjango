from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse(' <h1>Bienvenido puto a inicio</h1>')
    return render(request, 'home.html', {'name':'John Ace'})