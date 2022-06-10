#from django.http import HttpResponse
from django.shortcuts import render

def greeting(request):
  context = {
    'greeting' : 'Olá! Este é um exemplo de uso de templates. :)'
  }
  return render(request, 'greeting.html', context)