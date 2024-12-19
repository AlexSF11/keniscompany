# A função render permite renderizar uma página HTML
from django.shortcuts import render, redirect, get_list_or_404
from django.http import JsonResponse
from .models import Produtos
from .models import Vendas
from .forms import ProdutoForm
from .forms import VendaForm


def produtos(request):
    dados = {
        'dados':Produtos.objects.all()
    }
    return render(request, 'produtos/produtos.html', context=dados)

def vendas(request):
    dados = {
        'dados':Vendas.objects.all()
    }
    return render(request, 'produtos/vendas.html', context=dados)

def vender(request):

    if request.method == "GET":
           
        form = VendaForm()
        context = {
            'form': form
        }
        return render(request, 'produtos/form_vendas.html', context=context)
    
        
    else:
        form = VendaForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = VendaForm()
        
        context = {
                'form': form
        }
        #return render(request, 'produtos/form_vendas.html', context=context)   
        return redirect('vendas') 


def estornar(request, id_venda):
    venda = Vendas.objects.get(pk=id_venda)
    if request.method == 'POST':
        
         # Atualizar o estoque do produto
        produto = venda.produto
        produto.estoque += venda.quantidade
        produto.save()

        venda.delete()
        return redirect('vendas')
    return render(request, 'produtos/confirmar_estorno.html', {'item': venda})


def form_produtos(request):
    if request.method == "GET":
           
        form = ProdutoForm()
        context = {
            'form': form
        }
        return render(request, 'produtos/form_produtos.html', context=context)
    else:
        form = ProdutoForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ProdutoForm()
        
        context = {
                'form': form
        }
        #return render(request, 'produtos/form_produtos.html', context=context) 
        return redirect('produtos')      



def editar(request, id_produto):
    produto = Produtos.objects.get(pk=id_produto)
    # novo_investimento/1 -> GET
    if request.method == 'GET':
        form = ProdutoForm(instance=produto)
        return render(request, 'produtos/form_produtos.html', {'form': form})
    # caso requisição seja POST
    else:
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
        return redirect('produtos')

#@login_required
def excluir(request, id_produto):
    produto = Produtos.objects.get(pk=id_produto)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos')
    return render(request, 'produtos/confirmar_exclusao.html', {'item': produto})



