from django.db import models

# Modelo para Estudiantes
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para Profesores
class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para Tareas
class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='tareas/')  # Usar FileField para manejar los archivos subidos
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class EntregaTarea(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='entregas/', null=True, blank=True)  # Cambiado a FileField
    fecha_entrega = models.DateTimeField()
    comentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Entrega de {self.estudiante} para {self.tarea}"
