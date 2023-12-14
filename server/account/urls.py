from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView , TokenBlacklistView

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('user/', views.detail, name='detail'),
    path('logout/', TokenBlacklistView.as_view(),  name='token_blacklist'),

]