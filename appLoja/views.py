from rest_framework import viewsets

from appLoja.models import Produto, Categoria, Venda
from appLoja.serializers import ProdutoSerializer, CategoriaSerializer, VendaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """
        Endpoint para criar, editar e deletar Produtos
    """

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """
        Endpoint para criar, editar e deletar Categorias
    """

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    

class VendaViewSet(viewsets.ModelViewSet):
    """
        Endpoint para criar, editar e deletar Vendas
    """

    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
