from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import re_path
from . import views
from django.urls import path, include

schema_view = get_schema_view(
   openapi.Info(
      title="SaveIt API",
      default_version='V3',
      description="SaveIt API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="SaveIt@google.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'apiSaveIt'

urlpatterns = [

    path('categorias/', views.criar_categoria),
    path('categorias/<int:categoria_id>/', views.CategoriasDetalhe.as_view()),
    path('sub_categorias/', views.criar_subcategoria),
    path('sub_categorias/<int:sub_categoria_id>/', views.SubCategoriaDetalhe.as_view()),
    path('planeamentos/', views.criar_planeamento),
    path('planeamentos/<int:planeamento_id>/', views.PlaneamentosDetalhe.as_view()),
    path('contas/', views.criar_conta),
    path('contas/<int:conta_id>/', views.ContasList.as_view()),
    path('investimento/', views.criar_invest),
    path('investimento/<int:invest_id>/', views.InvestDetalhes.as_view()),
    path('registo/', views.criar_registo),
    path('registo/<int:registo_id>/', views.RegistoDetalhes.as_view()),
    path('alertas/', views.criar_alert),
    path('alertas/<int:alert_id>/', views.AlertaDetalhes.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]




