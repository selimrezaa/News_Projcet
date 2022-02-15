from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from news_app.models import *
from news_app.forms import *

from django.http.response import JsonResponse
from rest_framework.views import APIView


# Create your views here.


def user_signup(request):
    form = CreateNewUser()
    register = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            form.save()
            register=True
            return HttpResponseRedirect('signup done')

    return render(request, 'news_app/user_signup.html', context={'form':form})


def user_login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
               
                return HttpResponse('login done')

    return render(request, 'news_app/user_login.html', context={'form':form})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse('logout successfully')
    else:
        return HttpResponseRedirect(reverse('app_login:user_signup'))


def home(request):
    news_obj = News.objects.all()
    return render(request, 'news_app/news.html', context={'news_obj': news_obj})

def add_news(request):
    form = AddNews()
    diction = {'form': form }
    if request.method=="POST":
        form = AddNews(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')

    return render(request, 'news_app/add_news.html', context=diction)



#category and subcategory 
from django.http.response import JsonResponse

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
class CategoryList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        category=request.data['category']
        sub_category={}
        if category:
            sub_categories=Category.objects.get(id=category).categories.all()
            sub_category={p.name:p.id for p in sub_categories}
        return JsonResponse(data=sub_category, safe=False)