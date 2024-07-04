# Importa a classe HttpResponse do Django, usada para retornar respostas HTTP simples
from django.http import HttpResponse  

# Importa a classe base generic do módulo de views genéricas do Django
from django.views import generic  

# Define uma classe de visualização baseada em classe que herda de generic.View
class PostView(generic.View):
    # Define um método GET que será chamado quando uma requisição GET for feita a esta view
    def get(self, request, *args, **kwargs):
        # Retorna uma resposta HTTP simples com o texto 'Hello World'
        return HttpResponse('Hello World')
