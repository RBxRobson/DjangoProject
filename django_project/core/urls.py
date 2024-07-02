# Importa o módulo admin do Django, que fornece a interface de administração do site
from django.contrib import admin  

# Importa as funções include e path do Django, usadas para definir e incluir URLs
from django.urls import include, path  

# Define a lista de padrões de URL para o projeto
urlpatterns = [
    # Mapeia a URL 'admin/' para a interface de administração do Django
    path('admin/', admin.site.urls),
    
    # Inclui as URLs definidas no módulo blog.urls sob o caminho 'home'
    # Isso significa que qualquer URL que comece com 'home' será tratada pelo módulo blog.urls
    path('home', include('blog.urls'))
]
