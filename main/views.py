from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from main.serializers import UserSerializer, GroupSerializer
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm
from .forms import *
from .models import *


# Create your views here.
class HomepageView(View):
    def get(self, request):
        return render(request, 'main/homepage.html',{})

class DatabaseView(View):
    def get(self,request):
        form = DatabaseForm
        databases = Database.objects.all()
        return render(request, 'dataset/database.html', {'databases': databases,
                                                         'form':form})

class DatasetListView(View):
    def get(self, request, database):
        datasets = Dataset.objects.all()
        return render(request, 'dataset/dataset.html', {'datasets':datasets})

class DatasetDetailView(View):
    def get(self, request, database, dataset):
        return render(request, 'dataset/dataset_detail.html', {})

class FavouriteDatasetView(View):
    def get(self,request,database, dataset):
        datasets = Dataset.objects.all()
        return render(request, 'dataset/dataset.html', {})

# class UploadDataset(View):
#     def get(self, request):
#     def post(self, request):

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect("main:login")

class LoginView(View):
    # def get(self,request):
    #     if request.user.id is not None:
    #         messages.error(request, str(request.user.id))
    #         return redirect(reverse(''))
    def get(self, request):

        form = AuthenticationForm()
        return render(request, "main/login.html", {"form": form})

    def post(self,request):
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f"YOu are now logged in as {username}")
            # return redirect(reverse('main:homepage'))
        form = AuthenticationForm()
        return render(request, "main/login.html", {"form": form})

class RegisterView(View):
    def get(self,request):
        form = NewUserForm
        return render(request=request,
                      template_name="main/register.html",
                      context={"form": form})
    def post(self, request):
        form = NewUserForm(request.POST)
        form = NewUserForm
        return render(request=request,
                      template_name="main/register.html",
                      context={"form": form})
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer