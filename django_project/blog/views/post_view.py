# Importando o módulo generic do Django, que fornece views genéricas.
from django.views import generic
# Importando o modelo Post que será utilizado nas views.
from blog.models import Post

# Classe de view genérica para listar objetos Post.
class PostView(generic.ListView):
    # Define o queryset que será utilizado para buscar os objetos Post.
    # Filtra os posts com status igual a 1 e ordena-os pela data de criação em ordem decrescente.
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    # Define o template que será utilizado para renderizar a página de lista de posts.
    template_name = "index.html"

# Classe de view genérica para exibir detalhes de um objeto Post específico.
class PostDetail(generic.DetailView):
    # Define o modelo que será utilizado para buscar o objeto específico.
    model = Post
    # Define o template que será utilizado para renderizar a página de detalhes do post.
    template_name = "post_detail.html"
