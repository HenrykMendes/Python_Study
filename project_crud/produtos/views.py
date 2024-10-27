from django.shortcuts import render, redirect, get_object_or_404;
from .models import Produtos;
from .forms import ProdutosForm

#lista de produtos
#"def" é um tipo de função que não necessita de classe e que pode ser chamada diretamente, não precisando ser instanciada.
def lista_produtos (request):
    Produtos = Produtos.object.all()
    return render (request, 'produtos/lista_produps.html')

# Create your views here.
