from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
#from django.template import render
from .forms import registroForm,cursoForm
from .models import Alumno, Curso
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def index (request):
    return render(request,'index.html')

def nosotros(request):
    return render (request,'nosotros.html')

def microsoldadura(request):

    # cursos= Curso.objects.all()

    data={
        'form':cursoForm()
    }
    if request.method=='POST':
        formulario = cursoForm(request.POST)
        if formulario.is_valid():
            formulario.save()

    

    return render (request,'microsoldadura.html',data)




def listar_curso(request):
    cursos = Curso.objects.all()
    contexto ={'cursos':cursos}


    return render (request,'microsoldadura.html',contexto)




def electronica(request):
    return render (request,'electronica.html')

def drones(request):
    return render (request,'drones.html')

def reballing(request):
    return render (request,'reballing.html')

def serviciotec(request):
    return render (request,'serviciotec.html')

def contacto(request):
    if request.method=="POST":

        subject=request.POST["nombre"]

        message=request.POST["email"] + " " + request.POST["telefono"]  + " " + request.POST["mensaje"]

        email_from=settings.EMAIL_HOST_USER

        recipient_list=["desarolloweb2020@gmail.com"]

        send_mail(subject,message,email_from,recipient_list)


        return render(request, 'gracias.html')

    return render (request,'contacto.html')

def login(request):
    form =UserCreationForm()
    context ={'form':form}






    return render (request,'login.html', context)

def recuperacionclave(request):
    return render (request,'recuperacionclave.html')





def registro(request):
    data={
        'form':registroForm()
    }

    if request.method=='POST':
        formulario = registroForm(request.POST)
        if formulario.is_valid():
            formulario.save()



    return render (request,'registro.html',data)






        # form = registroForm()
        # #contex_instance=RequestContext(request)
        # context= {'form' : form},













    # if request.method=='POST':
    #     form = formulario(request.POST)
    #     if form.is_valid():



    #         return HttpResponseRedirect('')
    #     else:
    #         form = formulario()
    #     return render(request,'registro.html',{})




    # def gracias(request):
    #     html = '<html><body>"por fin resulta esta mierda"</body><html>'
    #     return HttpResponse(html)














    #         return redirect('index')
    #     else:
    #         form=registroForm()
        #return render(request,)








    # else:
    #     form = registroForm()
    # retur render(request)




    # form=registroForm(request.POST or None)
    # if formulario.is_valid():
    #     form_data= form.cleaned_data
    #     nombre= form_data.get("nombre")
    #     apellido= form_data.get("")
    #     rut= form_data.get("apellido")
    #     email= form_data.get("email")
    #     contrasena= form_data.get("contrasena")
    #     obj= Alumno.objects.create( nombre = nombre, apellido = apellido , rut=rut , email=email , contrasena=contrasena)
    # context={
    #     "el_form":form,
    # }




    # if request.method=='POST':
    #     formulario =registroForm(request.POST)
    #     if formulario.is_valid():
    #         formulario.save()
    #         data['mensaje'] = "guardado correctamente XD "






    # return render (request,'registro.html',context)



