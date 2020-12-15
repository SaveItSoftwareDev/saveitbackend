from django.urls import path
from apiSaveIt.views import ProfileViewSet, PerfilView
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'apiSaveIt'

router = DefaultRouter()
router.register(r'', ProfileViewSet, basename='utilizador')
urlpatterns = [
    path('api/', PerfilView.as_view(), name="perfil")
]

urlpatterns = router.urls


