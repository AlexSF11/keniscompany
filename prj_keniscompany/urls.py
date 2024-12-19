"""
URL configuration for prj_keniscompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from keniscompany import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.produtos, name='produtos'),
    path('form_vendas/', views.vender, name='vender'),
    path('form_produtos/<int:id_produto>', views.editar, name='editar'),
    path('form_produtos/', views.form_produtos, name='form_produtos'),
    path('produtos/', views.produtos, name='produtos'),
    path('vendas/', views.vendas, name='vendas'),
    path('excluir_produto/<int:id_produto>', views.excluir, name='excluir'),
    path('estornar_venda/<int:id_venda>/', views.estornar, name='estornar')
]
