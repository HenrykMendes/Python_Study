from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
#importando o arquivo models da pasta produtos
#importando ProdutosForms da pasta forms
from .models import Produtos 
from .forms import ProdutosForm


def lista_produtos(request):
    