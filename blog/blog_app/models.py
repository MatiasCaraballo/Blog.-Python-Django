from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validar_caracter_especial(value):
    if any(not char.isalnum() and not char.isspace() for char in value):
        raise ValidationError('No puede contener caracteres especiales.')

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100,null=False,unique=True,verbose_name='nombre',validators =[validar_caracter_especial])
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'categories'
        verbose_name ='categorias'
        verbose_name_plural = 'categorias'
        ordering = ['id']
class Post(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank = True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    titulo = models.CharField(unique=True,max_length=100,null = False,verbose_name='Título') 
    contenido = models.TextField(null =True,verbose_name = "Contenido del post")
    imagen = models.ImageField(upload_to='posts/%Y/%m/%d',null = True, blank = True,verbose_name ='Imagen del post')
    fecha_alta = models.DateTimeField(auto_now_add=True,verbose_name='Fecha alta')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True,verbose_name='Fecha actualización')
    
    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'Post'
        verbose_name ='Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']