from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
#importando o arquivo models da pasta produtos
#importando ProdutosForms da pasta forms
from .models import Produtos 
from .forms import ProdutosForm

#lista de produtos
def lista_produtos(request):
    produto = Produtos.objects.all()
    return render (request, 'produto/lista_produtos.html') #criar a página html e retornar a página como resposta

#criar um produto
def criar_produto (request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect ('lista_produtos')
    
#editar um produto
def editar_produto (request, id):
    produto = get_object_or_404(Produtos, id = id)
    form = ProdutosForm (request.POST)
    if form.is_valid():
       form.save()
       return redirect ('lista_produtos')
    return render (request,'produtos/editar_produto', {'form':form, 'produto', produto})

#deletar produto
def deletar_produto (request, id):
    produto = get_object_or_404 (Produtos,id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render (request, 'produtos/deletar_produto.html', {'produto' : produto})