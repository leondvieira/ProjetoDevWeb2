
from rest_framework import viewsets, permissions

from appLoja.models import Produto, Categoria, Venda
from appLoja.serializers import ProdutoSerializer, CategoriaSerializer, VendaSerializer
from appLoja.permissions import IsOwner


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
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user.id)
