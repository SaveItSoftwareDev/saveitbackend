from django.urls import path
from .views import CategoriaViewSet, SubCategoriaViewSet, PlaneamentoViewSet, ContaViewSet, InvestViewSet, AlertViewSet, RegistoViewSet
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import re_path
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

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
urlpatterns = [

    path('categorias/', views.criar_categoria),
    path('categorias/<int:categoria_id>/', views.categoria_detalhe),
    path('sub_categorias/', views.criar_subcategoria),
    path('sub_categorias7<int:sub_categoria_id>', views.subcategoria_detalhe),
    path('planeamentos/', views.criar_planeamento),
    path('planeamentos/<int:planeamento_id>/', views.planeamento_detalhe),
    path('contas/', views.criar_conta),
    path('contas/<int:conta_id>/', views.conta_detalhe),
    path('investimento/', views.criar_invest),
    path('registo/', views.criar_registo),
    path('registo/<int:registo_id>/', views.invest_detalhe),
    path('alertas/', views.criar_alert),
    path('alertas/<int:alert_id>/', views.alert_detalhe),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

router = DefaultRouter()
router.register('categorias', CategoriaViewSet, basename='categoria_viewsets')
router.register('sub_categorias', SubCategoriaViewSet, basename='sub_categoria_viewsets')
router.register('planeamentos', PlaneamentoViewSet, basename='planeamento_viewsets')
router.register('contas', ContaViewSet, basename='contas_viewsets')
router.register('investimento', InvestViewSet, basename='investimento_viewsets')
router.register('registo', RegistoViewSet, basename='registo_viewsets')
router.register('alertas', AlertViewSet, basename='alertas_viewsets')
urlpatterns += router.urls


