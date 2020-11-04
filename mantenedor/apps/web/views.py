from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request,'index.html')

def nosotros(request):
    return render (request,'nosotros.html')

def microsoldadura(request):
    return render (request,'microsoldadura.html')

def electronica(request):
    return render (request,'electronica.html')

def drones(request):
    return render (request,'drones.html')    

def reballing(request):
    return render (request,'reballing.html')

def serviciotec(request):
    return render (request,'serviciotec.html')

def contacto(request):
    return render (request,'contacto.html')

def login(request):
    return render (request,'login.html')

def recuperacionclave(request):
    return render (request,'recuperacionclave.html')    

def registro(request):
    return render (request,'registro.html')  

