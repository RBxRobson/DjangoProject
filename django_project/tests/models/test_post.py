import pytest

from blog.factories import PostFactory

# Define uma fixture para o pytest que cria um post publicado usando a PostFactory
@pytest.fixture
def post_published():
    # Retorna uma instância de Post com o título 'pytest with factory'
    return PostFactory(title='pytest with factory')

# Marca este teste como um que deve acessar o banco de dados do Django
@pytest.mark.django_db
def test_create_published_post(post_published):
    # Verifica se o título do post publicado é igual a 'pytest with factory'
    assert post_published.title == 'pytest with factory'
