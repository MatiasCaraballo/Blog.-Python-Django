from rest_framework import serializers
from .models import Categoria, Post

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ['id','autor','categoria','titulo','contenido','imagen','fecha_alta','fecha_actualizacion']