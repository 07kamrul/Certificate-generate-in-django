from django.urls import path
from . import views

urlpatterns = [
    # path('generateCertificate/', views.generateCertificate, name="generateCertificate" ),
    # path('register/', views.generateCertificate, name="register" ),
    path('showCertificate/<str:pk_test>/', views.showCertificate, name="showCertificate"),
    path('', views.home, name="home"),

    path('createCertificate/', views.createCertificate, name="createCertificate"),

]