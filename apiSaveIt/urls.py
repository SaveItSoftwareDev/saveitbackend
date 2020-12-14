from django.urls import path
from apiSaveIt.views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProfileViewSet, basename='utilizador')
urlpatterns = router.urls


