from django.urls import path
from apiSaveIt.views import ProfileViewSet, CategoriaViewSet, SubCategoriaViewSet, PlaneamentoViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import re_path
from django.conf.urls import url
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="SaveIt API",
      default_version='V2',
      description="SaveIt API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="SaveIt@google.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

#app_name = 'apiSaveIt'

router = DefaultRouter()
router.register(r'', ProfileViewSet, basename='utilizador')
urlpatterns = [
    path('perfis/', views.criar_perfil),
    path('perfis/<int:perfil_id>/', views.perfil_detalhe),
    path('categorias/', views.criar_categoria),
    path('categorias/<int:categoria_id>/', views.categoria_detalhe),
    path('sub_categorias/', views.criar_subcategoria),
    path('sub_categorias7<int:sub_categoria_id>', views.subcategoria_detalhe),
    path('planeamentos/', views.criar_planeamento),
    path('planeamentos/<int:planeamento_id>/', views.planeamento_detalhe),
    path('contas/', views.criar_conta),
    path('contas/<int:conta_id>/', views.conta_detalhe),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
router = DefaultRouter()
router.register('perfis', ProfileViewSet, basename='perfil_viewsets')
router.register('categorias', CategoriaViewSet, basename='categoria_viewsets')
router.register('sub_categorias', SubCategoriaViewSet, basename='sub_categoria_viewsets')
router.register('planeamentos', PlaneamentoViewSet, basename='planeamento_viewsets')
router.register('contas', ContaViewSet, basename='contas_viewsets')
urlpatterns += router.urls


