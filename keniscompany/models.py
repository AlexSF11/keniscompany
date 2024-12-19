from django.db import models
from datetime import datetime

TAMANHO_CHOICES = (
    ('P', 'P'),
    ('M', 'M'),
    ('G', 'G'),
    ('GG', 'GG')
)

class Produtos(models.Model):
    camisa = models.TextField(unique=True, max_length=100)
    #versao = models.TextField(default=0)
    estoque = models.IntegerField()
    custo = models.FloatField()
    preco_venda = models.FloatField()
    tamanho = models.TextField(max_length=2, choices=TAMANHO_CHOICES)


    def decrease_stock(self, quantidade):
            self.estoque -= quantidade
            self.save()
    def __str__(self):
        return self.camisa
  

   
class Vendas(models.Model):
    cliente = models.TextField(max_length=100)
    quantidade = models.IntegerField(default=None)
    produto = models.ForeignKey(
    Produtos, on_delete=models.CASCADE, 
    related_name="produto", 
    to_field='camisa')
    data = models.DateField(default=datetime.now)

    def __str__(self):
        return self.produto

    def save(self, *args, **kwargs):
            """
            Reduz o estoque do produto ao salvar a saída.
            """
            if self.pk is None:  # Apenas na criação
                self.produto.decrease_stock(self.quantidade)
            super().save(*args, **kwargs)

    def estornar_venda(venda_id):
        from django.shortcuts import get_object_or_404

        # Obter a venda
        venda = get_object_or_404(Vendas, id=venda_id)

        # Verificar se já foi estornada
        #if venda.estornada:
            #raise ValueError("A venda já foi estornada.")

        # Atualizar o estoque do produto
        produto = venda.produto
        produto.estoque += venda.quantidade
        produto.save()



    
    

    
    



    



    
  
   