from django.forms import ModelForm
from .models import Produtos
from .models import Vendas

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = "__all__"
        #fields = ['camisa', 'versao', 'estoque', 'custo', 'preco_venda', 'tamanho']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['camisa'].widget.attrs.update({'placeholder': 'Digite o nome do produto'})
        #self.fields['versao'].widget.attrs.update({'placeholder': 'Digite o modelo do produto'})
        self.fields['estoque'].widget.attrs.update({'placeholder': 'Digite a quantidade em estoque'})
        self.fields['custo'].widget.attrs.update({'placeholder': 'Digite o custo do produto'})
        self.fields['preco_venda'].label = 'Preço de Venda'
        self.fields['preco_venda'].widget.attrs.update({'placeholder': 'Digite o preço de venda do produto'})
        self.fields['tamanho'].label = 'Tamanho do Produto'



class VendaForm(ModelForm):
    class Meta:
        model = Vendas
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs.update({'placeholder': 'Digite o nome do cliente'})
        self.fields['quantidade'].widget.attrs.update({'placeholder': 'Digite a quantidade do produto'})
        self.fields['produto'].label = 'Camisa'
        self.fields['data'].label = 'Data da Venda'

      