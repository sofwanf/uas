from django.shortcuts import render
from .models import pasien

def wawan(request):
    blog = pasien.objects.all()
    context = {
    'blog': blog, 
}

    return render(request,'pasien.html',context)