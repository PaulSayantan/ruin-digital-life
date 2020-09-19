# auth0authorization/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
    path('api/register',views.Register.as_view()),
    path('api/login',views.Login.as_view())
]