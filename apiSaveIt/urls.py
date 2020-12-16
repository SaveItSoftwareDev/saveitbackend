from django.urls import path
from apiSaveIt.views import ProfileViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import re_path
from django.conf.urls import url
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="SaveIt API yasg swagger",
      default_version='v1',
      description="SaveIt API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ljsgmg@google.com"),
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
    path('perfis/<str:perfil_id>/', views.perfil_detail),
    path('categorias/', views.criar_categoria),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]




from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
router = DefaultRouter()
router.register('perfis', ProfileViewSet, basename='perfil_viewsets')
urlpatterns += router.urls


