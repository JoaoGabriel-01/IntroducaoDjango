#from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

def greeting(request):
  context = {
    'greeting' : 'Olá! Este é um exemplo de uso de templates. :)',
    'today' : timezone.now()
  }
  return render(request, 'greeting.html', context)