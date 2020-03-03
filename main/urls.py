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
    path("datasets/", DatabaseView.as_view(), name="database"),
    path('member/register', RegisterView.as_view(), name='register'),
    path('member/login', LoginView.as_view(), name='login'),
    path('member/logout', LogoutView.as_view(), name='logout'),
    path('datasets/<database>', DatasetListView.as_view(), name='dataset_list'),
    path('datasets/<database>/<dataset>', DatasetDetailView.as_view(), name='dataset_detail'),
    path('datasets/<database>/<dataset>', FavouriteDatasetView.as_view(), name='favourite_dataset')

]