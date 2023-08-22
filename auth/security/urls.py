from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sign_up/', views.signup, name="signup"),
    path('sign_in/', views.signin, name="signin"),
    path('reset_password/', views.reset_password, name="reset_password"),
]
