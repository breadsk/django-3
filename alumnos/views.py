from django.shortcuts import render

from .models import Genero,Alumno
# Create your views here.

def index(request):
    #alumnos = Alumno.objects.all()
    #context = {"alumnos":alumnos}
    context={}
    return render(request,"alumnos/index.html",context)

def crud(request):
    alumnos = Alumno.objects.all()
    #alumnos = Alumno.objects.raw("SELECT * FROM alumnos_alumno")
    context = {"alumnos":alumnos}
    return render(request,"alumnos/alumnos_list.html",context)

def alumnosAdd(request):
    if request.method != "POST":
        print(request)
        #No es un post , por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context={"generos":generos}
        return render(request,"alumnos/alumnos_add.html",context)
    else:
        print("Entra por aqui")
        #Es un post , por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(
            rut = rut,
            nombre = nombre,
            apellido_paterno = aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo=1
        )
        obj.save()
        context = {"mensaje":"Ok , datos guardados....."}
        return render(request,"alumnos/alumnos_add.html",context)

def alumnos_del(request,pk):
    context = {}
    try:
        alumno=Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje = "Eliminado satisfactoriamente"
        alumnos = Alumno.objects.all()
        context = {'alumnos':alumnos , 'mensaje':mensaje}
        return render(request,"alumnos/alumnos_list.html",context)
    except:
        mensaje = "Error , rut no existe"
        alumnos = Alumno.objects.all()
        context = {'alumnos':alumnos , 'mensaje':mensaje}
        return render(request,"alumnos/alumnos_list.html",context)
    
def alumnos_findEdit(request,pk):
    
    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
        generos = Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context = {'alumno':alumno,'generos':generos}

        if alumno:
            return render(request,"alumnos/alumnos_edit.html",context)
        else:
            context={"mensaje":"Error, rut no existe"}
            return render(request,"alumnos/alumnos_edit.html",context)

def alumnosUpdate(request):
    if request.method == "POST":
        #Es un post, por lo tanto se recuperan los datos del formulario
        # y se graban en una tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        alumno = Alumno()
        alumno.rut = rut
        alumno.nombre = nombre
        alumno.apellido_paterno = aPaterno
        alumno.apellido_materno = aMaterno
        alumno.fecha_nacimiento = fechaNac        
        alumno.id_genero = objGenero
        alumno.telefono = telefono
        alumno.email = email
        alumno.direccion = direccion
        alumno.activo=1
        alumno.save()

        generos = Genero.objects.all()
        context = { "mensaje": "Datos actualizados satisfactoriamente", "generos":generos,"alumno":alumno }

        return render(request,"alumnos/alumnos_edit.html",context)
    else:
        #No es un post , por lo tanto se muestra el formulario para agregar
        alumnos = Alumno.objects.all()
        context = {"alumnos":alumnos}
        return render(request,"alumnos/alumnos_list.html",context)
    
def crud_generos(request):
    generos = Genero.objects.all()
    #generos = Genero.objects.raw("SELECT * FROM alumnos_alumno")
    context = {"generos":generos}
    return render(request,"alumno/generos_list.html",context)