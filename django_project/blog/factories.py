import factory
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from blog.models import Post

# Instância do Faker para gerar dados fictícios
faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        # Especifica o modelo que esta factory cria instâncias
        model = User  

    # Gera um email fictício seguro usando o Faker
    email = factory.Faker("safe_email")  
    
    # Gera um nome de usuário fictício usando o Faker
    username = factory.LazyAttribute(lambda x: faker.name())  

    @classmethod
    def _prepare(cls, create, **kwargs):

        # Remove a senha dos argumentos se fornecida
        password = kwargs.pop("password", None)  

        # Cria a instância do usuário
        user = super(UserFactory, cls)._prepare(create, **kwargs)  
        if password:
            
            # Define a senha usando o método apropriado
            user.set_password(password) 
            if create:
                
                # Salva o usuário no banco de dados se create for True
                user.save() 

        # Retorna a instância do usuário
        return user  

# Factory para criar instâncias do modelo Post
class PostFactory(factory.django.DjangoModelFactory):
    # Gera um título fictício
    title = factory.LazyAttribute(lambda x: faker.sentence())

    # Define a data de criação como o momento atual
    created_on = factory.LazyAttribute(lambda x: now())

    # Cria um autor usando a UserFactory
    author = factory.SubFactory(UserFactory)

    # Define o status padrão como 0 (Draft)
    status = 0  

    class Meta:

        # Especifica o modelo que esta factory cria instâncias
        model = Post 
