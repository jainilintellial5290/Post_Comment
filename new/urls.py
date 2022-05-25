from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login,name="login"),
    path('signup/', views.signup, name="signup"),
    path('comment/', views.comment,name="comment"),
    path('compose/', views.compose,name="compose"),
    path('like/', views.like, name="like"),
]


