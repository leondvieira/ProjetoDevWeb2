from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

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


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(usuario=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        id_produto = serializer.data.get("produto")
        produto = Produto.objects.get(id=id_produto)
        if produto.unidade < serializer.data.get("quantidade"):
            return Response({"details": "Quantidade não disponível no estoque."}, status.HTTP_403_FORBIDDEN)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
