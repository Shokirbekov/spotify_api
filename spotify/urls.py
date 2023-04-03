from asosiy.views import *
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("qoshiqchilar", QoshiqchilarViewSet)
router.register("albomlar", AlbomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('qoshiqlar/', QoshiqAPIView.as_view()),
]