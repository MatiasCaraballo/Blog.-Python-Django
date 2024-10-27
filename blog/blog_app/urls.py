from rest_framework import routers
from .views import PostViewSet, CategoriaViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('categorias', CategoriaViewSet, basename='categoria')

urlpatterns = router.urls
