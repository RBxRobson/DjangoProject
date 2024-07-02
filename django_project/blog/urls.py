# Importa a função path do Django, que é usada para definir URLs
from django.urls import path  

# Importa o módulo views do aplicativo blog
from blog import views  

# Define a lista de padrões de URL para o aplicativo
urlpatterns = [
    # Mapeia a URL raiz ('') para a view PostView, 
    # usando a função as_view() para retornar a view 
    # baseada em classe como uma view baseada em função
    # O nome da URL é 'home', que pode ser usado 
    # para referenciar essa URL em outras partes do código
    path('', views.PostView.as_view(), name='home')
]
