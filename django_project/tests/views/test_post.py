# Importa o módulo pytest, que é uma ferramenta para testar código Python
import pytest  

# Importa a função reverse do Django, 
# que é usada para construir URLs a partir dos nomes de suas visualizações (views)
from django.urls import reverse  


# Decorador pytest.mark.django_db indica que o teste deve acessar o banco de dados
@pytest.mark.django_db
def test_post_view(client):
    # Usa a função reverse para obter a URL da visualização nomeada 'home'
    url = reverse('home')
    
    # Faz uma requisição GET à URL obtida
    response = client.get(url)
    
    # Verifica se o código de status da resposta é 200 (OK) 
    # e se a pagina tem o conteúdo textual "Welcome to my awesome Blog"
    assert response.status_code == 200
    assert b'Welcome to my awesome Blog' in response.content