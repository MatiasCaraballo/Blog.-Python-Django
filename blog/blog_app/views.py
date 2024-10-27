from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets,routers
from .models import Post,Categoria
from .serializers import PostSerializer,CategoriaSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

router = routers.DefaultRouter(viewsets.ModelViewSet)
router.register('posts',PostViewSet,basename ='post')
urlpatterns = router.urls
