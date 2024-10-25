from django import forms
from .models import Produtos

class ProdutosForm (forms.ModelForm):
    class meta:
        model = Produtos
        fields = ['nome', 'descricao', 'preco', 'estoque']