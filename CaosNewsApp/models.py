from django.db import models

class Noticia(models.Model):
    id_noticia  = models.AutoField(db_column='id_noticia', primary_key=True) 
    titulo_noticia = models.CharField(max_length=20, blank=False, null=False)
    subtitulo_noticia = models.CharField(max_length=50, blank=False, null=False)
    cuerpo_noticia = models.CharField(max_length=999999, blank=False, null=False)
    activo = models.BooleanField(default='000000')

    def __str__(self):
        return str(self.titulo_noticia)
   
'''class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.IntegerField()
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)
'''