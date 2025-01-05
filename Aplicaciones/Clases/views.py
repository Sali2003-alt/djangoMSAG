from django.shortcuts import render, redirect
from .models import Tarea, Profesor
from .models import Estudiante
from .models import EntregaTarea
from .forms import EntregaTareaForm  # Asumiendo que tienes un formulario para EntregaTarea
from .forms import TareaForm
from django.db.models import Max 
from django.shortcuts import get_object_or_404
from django.contrib import messages



#Funcion para presentar en pantalla (renderizar) el codigo html del template inicio.html
def inicio(request):
    return render(request,'inicio.html')

def nuevoEstudiante(request):
    # Buscar el último ID en la base de datos
    ultimo_id = Estudiante.objects.aggregate(Max('id'))['id__max']

    
    # Si no existe ningún registro, asignar el ID como 1
    nuevo_id = ultimo_id + 1 if ultimo_id else 1

    # Renderizar la plantilla con el nuevo ID
    return render(request, 'nuevoEstudiante.html', {'id': nuevo_id})

def guardarEstudiante(request):
    if request.method == "POST":
        nombre = request.POST['txt_nombre']
        apellido = request.POST['txt_apellido']
        email = request.POST['txt_email']
        telefono = request.POST['txt_telefono']
        
        # Guardar el nuevo estudiante
        nuevoEstudiante = Estudiante.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )

        messages.success(request, "Estudiante Guardado Exitosamente")
        return redirect('/listadoEstudiante')

def listadoEstudiante(request):
    estudiantesBdd = Estudiante.objects.all()
    return render(request, 'listadoEstudiante.html', {'estudiantes': estudiantesBdd})

from django.shortcuts import get_object_or_404

def eliminarEstudiante(request, id):
    estudianteEliminar = get_object_or_404(Estudiante, id=id)
    estudianteEliminar.delete()
    messages.success(request, "Estudiante Eliminado")
    return redirect('/listadoEstudiante')

# Función para mostrar el formulario de edición
def editarEstudiante(request, id):
    estudianteEditar = get_object_or_404(Estudiante, id=id)
    return render(request, "editarEstudiante.html", {'estudiante': estudianteEditar})


# Función para procesar la edición del estudiante
def procesarEdicionEstudiante(request):
    # Obtener el estudiante por el ID
    estudiante = Estudiante.objects.get(id=request.POST['id'])
    # Obtener los datos del formulario
    nombre = request.POST['txt_nombre']
    apellido = request.POST['txt_apellido']
    email = request.POST['txt_email']
    telefono = request.POST['txt_telefono']
    estudiante.nombre = nombre
    estudiante.apellido = apellido
    estudiante.email = email
    estudiante.telefono = telefono
    # Guardar los cambios en la base de datos
    estudiante.save()
    messages.success(request, "Estudiante Editado Exitosamente")
    return redirect('/listadoEstudiante')


    
   

#PROFESOR
# Presentando en pantalla el formulario para un nuevo Profesor
def nuevoProfesor(request):
    # Buscar el último ID en la base de datos
    ultimo_id = Profesor.objects.aggregate(Max('id'))['id__max']

    
    # Si no existe ningún registro, asignar el ID como 1
    nuevo_id = ultimo_id + 1 if ultimo_id else 1

    # Renderizar la plantilla con el nuevo ID
    return render(request, 'nuevoProfesor.html', {'id': nuevo_id})


# Listado de Profesores
def listadoProfesor(request):
    profesoresBdd = Profesor.objects.all()
    return render(request, 'listadoProfesor.html', {'profesores': profesoresBdd})


# Capturando datos del formulario e insertando en la Base de Datos
def guardarProfesor(request):
    if request.method == "POST":
        nombre = request.POST['txt_nombre']
        apellido = request.POST['txt_apellido']
        email = request.POST['txt_email']
        telefono = request.POST['txt_telefono']
        
        # Guardar el nuevo profesor
        nuevoProfesor = Profesor.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )

        messages.success(request, "Profesor Guardado Exitosamente")
        return redirect('/listadoProfesor')


# Función para eliminar un profesor por ID
def eliminarProfesor(request, id):
    profesorEliminar = get_object_or_404(Profesor, id=id)
    profesorEliminar.delete()
    messages.success(request, "Profesor Eliminado")
    return redirect('/listadoProfesor')




def editarProfesor(request, id):
    profesorEditar = Profesor.objects.get(id=id)
    return render(request, 'editarProfesor.html', {'profesor': profesorEditar})


def procesarEdicionProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    nombre = request.POST['txt_nombre']
    apellido = request.POST['txt_apellido']
    email = request.POST['txt_email']
    telefono = request.POST['txt_telefono']
    
    # Asignar los datos obtenidos a los campos del profesor
    profesor.nombre = nombre
    profesor.apellido = apellido
    profesor.email = email
    profesor.telefono = telefono
    
    # Guardar los cambios en la base de datos
    profesor.save()
    
    messages.success(request, "Profesor Editado Exitosamente")
    return redirect('/listadoProfesor')

# Tareas

def nuevaTarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES.get('archivo')  # Obtén el archivo
            if archivo and archivo.name.endswith('.mp4'):
                # Guardar la tarea
                form.save()
                messages.success(request, "Tarea creada exitosamente.")
                return redirect('/listadoTarea')
            else:
                messages.error(request, "El archivo debe ser un .mp4")
        else:
            messages.error(request, "Formulario inválido")
    else:
        form = TareaForm()

    return render(request, 'nuevaTarea.html', {'form': form, 'profesores': Profesor.objects.all()})


# Listado de tareas
def listadoTarea(request):
    tareasBdd = Tarea.objects.select_related('profesor').all()
    return render(request, 'listadoTarea.html', {'tareas': tareasBdd})

# Guardar nueva tarea
def guardarTarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        profesor_id = request.POST.get('profesor')
        archivo = request.FILES.get('archivo')

        # Guardar tarea
        Tarea.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            archivo=archivo,
            profesor_id=profesor_id
        )
        messages.success(request, "Tarea guardada exitosamente.")
        return redirect('/listadoTarea')

# Eliminar una tarea por su ID
def eliminarTarea(request, id):
    tareaEliminar = get_object_or_404(Tarea, id=id)
    tareaEliminar.delete()
    messages.success(request, "Tarea eliminada exitosamente.")
    return redirect('/listadoTarea')

# Mostrar el formulario para editar una tarea

def editarTarea(request, id):
    tareaEditar = Tarea.objects.get(id=id)
    profesores = Profesor.objects.all()
    return render(request, 'editarTarea.html', {'tarea': tareaEditar, 'profesores': profesores})






# Procesar la edición de una tarea
def procesarEdicionTarea(request):
    
    tarea = Tarea.objects.get(id=request.POST['id'])
    tarea.titulo = request.POST.get('txt_titulo')
    tarea.descripcion = request.POST.get('txt_descripcion')
    archivo = request.FILES.get('txt_archivo')

    # Actualizar el archivo solo si se sube uno nuevo
    if archivo:
        tarea.archivo = archivo

    tarea.profesor_id = request.POST.get('txt_profesor')
    

    tarea.save()

    messages.success(request, "Tarea editada exitosamente.")
    return redirect('/listadoTarea')


def procesarEdicionTarea(request):
    if request.method == 'POST':
        # Obtener la tarea que se va a editar
        tarea_id = request.POST.get('id')  # Asegúrate de que el campo ID esté en el formulario
        
        if not tarea_id:
            return HttpResponse("Error: ID de tarea no proporcionado.", status=400)

        try:
            tarea = Tarea.objects.get(id=tarea_id)
        except Tarea.DoesNotExist:
            return HttpResponse("Error: Tarea no encontrada.", status=404)

        # Usar el formulario para validar y guardar los datos
        form = TareaForm(request.POST, request.FILES, instance=tarea)
        
        if form.is_valid():
            # Si el formulario es válido, se guarda la tarea
            form.save()
            messages.success(request, "Tarea editada exitosamente.")
            return redirect('/listadoTarea')
        else:
            # Si el formulario no es válido, se muestran los errores
            messages.error(request, "Error al editar la tarea. Verifique los datos.")
            return redirect('/editarTarea/' + tarea_id)
    
    return HttpResponse("Método no permitido", status=405)
#Entregas
def nuevaEntrega(request):
    if request.method == "POST":
        form = EntregaTareaForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar la nueva entrega
            form.save()
            messages.success(request, "Entrega registrada exitosamente.")
            return redirect('listadoEntrega')  # Redirigir al listado de entregas
        else:
            messages.error(request, "Error al registrar la entrega. Verifique los campos.")
    else:
        form = EntregaTareaForm()

    return render(request, 'nuevaEntrega.html', {'form': form})

def listadoEntrega(request):
    entregas = EntregaTarea.objects.all()
    return render(request, 'listadoEntrega.html', {'entregas': entregas})

# Guardar una nueva entrega
def guardarEntrega(request):
    if request.method == "POST":
        form = EntregaTareaForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Crear la nueva entrega con los datos del formulario
            form.save()

            # Mensaje de éxito
            messages.success(request, "Entrega guardada exitosamente")
            return redirect('/listadoEntrega')  # Redirige a la lista de entregas
        else:
            # Mensaje de error en caso de que el formulario no sea válido
            messages.error(request, "Error al guardar la entrega")
            return redirect('/nuevaEntrega')  # Redirige al formulario para intentar nuevamente

    else:
        messages.error(request, "Error al recibir los datos")
        return redirect('/nuevaEntrega')  # Si no es un POST, redirige al formulario


def editarEntrega(request, id):
    entrega = EntregaTarea.objects.get(id=id)
    if request.method == "POST":
        form = EntregaTareaForm(request.POST, request.FILES, instance=entrega)
        if form.is_valid():
            form.save()
            messages.success(request, "Entrega actualizada exitosamente.")
            return redirect('/listadoEntrega')
        else:
            messages.error(request, "Error al actualizar la entrega.")
    else:
        form = EntregaTareaForm(instance=entrega)

    return render(request, 'editarEntrega.html', {'form': form})



def procesarEdicionEntrega(request):
    if request.method == "POST":
        entrega = EntregaTarea.objects.get(id=request.POST['id'])
        entrega.estudiante = Estudiante.objects.get(id=request.POST['estudiante'])
        entrega.tarea = Tarea.objects.get(id=request.POST['tarea'])
        entrega.archivo = request.FILES['archivo']
        entrega.comentario = request.POST['comentario']
        entrega.save()

        messages.success(request, "Entrega editada exitosamente.")
        return redirect('/listadoEntrega')
    else:
        messages.error(request, "Error al editar la entrega.")
        return redirect('/listadoEntrega')


def eliminarEntrega(request, id):
    entrega = get_object_or_404(EntregaTarea, id=id)
    entrega.delete()  # Elimina la entrega
    return redirect('/listadoEntrega')  # Redirige al listado de entregas
