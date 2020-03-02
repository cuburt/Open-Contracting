from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("home/", HomepageView.as_view(), name="homepage"),
]