from django.urls import path
from .views import index, nosotros, microsoldadura, electronica, drones, reballing, serviciotec, contacto, login, recuperacionclave, registro


urlpatterns = [
    path('',index, name= 'index'),
    path('nosotros/', nosotros, name= 'nosotros'),
    path('microsoldadura/', microsoldadura, name= 'microsoldadura'),
    path('electronica/', electronica, name= 'electronica'),
    path('drones/', drones, name= 'drones'),
    path('reballing/', reballing, name= 'reballing'),
    path('serviciotec/', serviciotec, name= 'serviciotec'),
    path('contacto/', contacto, name= 'contacto'),
    path('login/', login, name= 'login'),
    path('recuperacionclave/', recuperacionclave, name= 'recuperacionclave'),
    path('registro/', registro, name= 'registro'),
    
]
