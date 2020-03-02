from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from main.serializers import UserSerializer, GroupSerializer
from django.views import View

# Create your views here.
class HomepageView(View):
    def get(self, request):
        return render(request, 'main/homepage.html',{})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer