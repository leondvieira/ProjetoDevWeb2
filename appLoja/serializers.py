from django.utils.translation import gettext as _
from rest_framework import serializers

from appLoja.models import Produto, Categoria, Venda


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = "__all__"

    def validate(self, attrs):
        produto = attrs.get('produto')
        if produto.unidade < attrs.get('quantidade'):
            raise serializers.ValidationError({"quantidade": _("Not available quantity in stock.")})  
        return super().validate(attrs)
