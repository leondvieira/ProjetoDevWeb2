from rest_framework import viewsets
from appLoja.models import Produto, Categoria, Venda


class ProdutoViewSet(viewsets.ModelViewSet):
    """
        Endpoint para criar, editar e deletar Produtos
    """
    
    queryset = Produto.objects.filter(active=True)
