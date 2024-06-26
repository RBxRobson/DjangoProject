from django.db import models
from django.contrib.auth.models import User

# Definindo as escolhas de status para os posts
STATUS = (
    (0, "Draft"),  # Rascunho
    (1, "Publish") # Publicado
)

class Post(models.Model):
    # Título do post, deve ser único
    title = models.CharField(max_length=200, unique=True)

    # Slug do post, usado para URLs amigáveis, deve ser único
    slug = models.SlugField(max_length=200, unique=True)

    # Autor do post, relacionado ao modelo User do Django, com relacionamento de muitos-para-um
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    # Data e hora da última atualização do post, atualizada automaticamente
    updated_on = models.DateTimeField(auto_now=True)

    # Conteúdo do post
    content = models.TextField()

    # Data e hora de criação do post, definida automaticamente na criação
    created_on = models.DateTimeField(auto_now_add=True)

    # Status do post, pode ser "Rascunho" (0) ou "Publicado" (1)
    status = models.IntegerField(choices=STATUS, default=0)

    # Meta informações sobre o modelo
    class Meta:
        # Ordenar os posts pela data de criação em ordem decrescente
        ordering = ['-created_on']

    # Método que retorna uma string representando o objeto, neste caso o título do post
    def __str__(self):
        return self.title
