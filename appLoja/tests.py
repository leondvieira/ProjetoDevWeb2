from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from appLoja.models import Produto, Venda, Categoria


class ProdutoAPITest(APITestCase):
    url = '/produtos/'

    def setUp(self):
        categoria = Categoria.objects.create(nome="Categoria Teste")
        Produto.objects.create(
            nome='Teste Produto',
            unidade=10,
            preco=20.50,
            ativo=True,
            categoria=categoria
        )

    def test_get_produtos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_produto(self):
        categoria = Categoria.objects.first()

        data = {
            'nome': 'Teste Produto',
            'unidade': 10,
            'preco': 20.50,
            'ativo': True,
            'categoria': categoria.id
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_produto(self):
        categoria = Categoria.objects.first()
        produto = Produto.objects.first()

        body = {
            'nome': 'Novo nome',
            'unidade': 15,
            'preco': 30.10,
            'ativo': False,
            'categoria': categoria.id
        }
        response = self.client.put(f'{self.url}{produto.id}/', body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_produto(self):
        produto = Produto.objects.first()
        response = self.client.delete(f'{self.url}{produto.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CategoriaAPITest(APITestCase):
    url = '/categorias/'

    def setUp(self):
        Categoria.objects.create(nome="Categoria Teste")

    def test_get_categorias(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_categoria(self):
        data = {
            'nome': 'Teste Categoria',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_categoria(self):
        categoria = Categoria.objects.first()
        body = {
            'nome': 'Novo nome',
        }
        response = self.client.put(f'{self.url}{categoria.id}/', body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_categoria(self):
        categoria = Categoria.objects.first()
        response = self.client.delete(f'{self.url}{categoria.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class VendaAPITest(APITestCase):
    url = '/vendas/'

    def setUp(self):
        categoria = Categoria.objects.create(nome="Categoria Teste")
        produto = Produto.objects.create(
            nome='Teste Produto',
            unidade=10,
            preco=20.50,
            ativo=True,
            categoria=categoria
        )
        usuario = User.objects.create(username='usuarioteste', password='senhateste')
        Venda.objects.create(
            produto=produto,
            quantidade=5,
            usuario=usuario
        )

    def test_authentiated_get_vendas(self):
        self.client.force_authenticate(user=User.objects.first())
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_get_vendas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_venda(self):
        self.client.force_authenticate(user=User.objects.first())
        produto = Produto.objects.first()
        usuario = User.objects.first()

        data = {
            'produto': produto.id,
            'quantidade': 5,
            'usuario': usuario.id
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_venda(self):
        self.client.force_authenticate(user=User.objects.first())
        produto = Produto.objects.first()
        usuario = User.objects.first()
        venda = Venda.objects.first()

        data = {
            'produto': produto.id,
            'quantidade': 10,
            'usuario': usuario.id
        }
        response = self.client.put(f'{self.url}{venda.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_venda(self):
        self.client.force_authenticate(user=User.objects.first())
        venda = Venda.objects.first()
        response = self.client.delete(f'{self.url}{venda.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
