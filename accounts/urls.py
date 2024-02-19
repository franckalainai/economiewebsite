from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/',views.author_register.as_view(), name='register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),

]