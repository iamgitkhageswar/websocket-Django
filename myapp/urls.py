
from django.urls import path, include
from .views import index, YourModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'yourmodel', YourModelViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
