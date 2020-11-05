from django.contrib import admin
from .models import Alumno, Curso, Contacto

# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","rut","email","contrasena")
    search_fields=("nombre","apellido","rut","email","contrasena")

class CursoAdmin(admin.ModelAdmin):
    list_display=("nombreCurso","modelaidad","valor","alumno")
    search_fields=("nombreCurso","modelaidad","valor","alumno")
    list_filter=("nombreCurso","modelaidad")


class ContactoAdmin(admin.ModelAdmin):
    list_display=("nombre","email","telefono","mensaje")
    search_fields=("nombre","email","telefono","mensaje")


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Curso, CursoAdmin )
admin.site.register(Contacto, ContactoAdmin)
