"""projeto_invista_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from invista_me import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # investimentos
    path('', views.investimentos, name='investimentos'),
    path('novo_investimento/', views.criarInvestimento, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>',
         views.editarInvestimento, name='editarInvestimento'),
    path('excluir_investimento/<int:id_investimento>',
         views.excluirInvestimento, name='excluirInvestimento'),
    path('investimento/<int:id_investimento>', views.detalheInvestimento,
         name='detalheInvestimento'),

    # gastos
    path('gastos/', views.gastos, name='gastos'),
    path('novo_gasto/', views.criarGasto, name='novo_gasto'),
    path('novo_gasto/<int:id_gasto>', views.editarGasto, name='editarGasto'),
    path('excluir_gasto/<int:id_gasto>',
         views.excluirGasto, name='excluirGasto'),
    path('gasto/<int:id_gasto>', views.detalheGasto, name='detalheGasto'),
]
