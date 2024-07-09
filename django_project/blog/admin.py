from django.contrib import admin

# Importa o modelo Post do módulo models
from .models import Post

# Cria uma classe para customizar a administração do modelo Post
class PostAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de posts no admin
    list_display = ('title', 'slug', 'status', 'created_on')
    # Adiciona filtros baseados no campo 'status'
    list_filter = ('status',)
    # Habilita a busca nos campos 'title' e 'content'
    search_fields = ['title', 'content']
    # Preenche automaticamente o campo 'slug' com base no campo 'title'
    prepopulated_fields = {'slug': ('title',)}

# Registra o modelo Post e a classe PostAdmin na interface de administração
admin.site.register(Post, PostAdmin)
