from django.contrib import admin
from django.urls import path
from news_app import views
from django.views.decorators.csrf import csrf_exempt
app_name = 'news_app'

urlpatterns = [
            path('home/', views.home, name='home'),
            path('add/', views.add_news, name='add_news'),
            path('user-login/', views.user_login, name='user_login'),
            path('user-signup/', views.user_signup, name='user_signup'),
            path('category/', views.CategoryList.as_view()),
]