from django.shortcuts import render
from.forms import formdaftar


def daftar(request):
    form = formdaftar()
    
    kontext = {
        'form' : form,
    }
    return render(request,'daftar.html',kontext)
