from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from ..models import Post

class PostVistasTest(TestCase):
    @classmethod
    def setUpTestData(cls):# inicializa los datos de prueba, base de datos
        # Set up non-modified objects used by all test methods
        u = User.objects.create(first_name='Lui', last_name='Bob')
        for x in range(20):# crea 20 posts
            Post.objects.create(title=f'My first post {x}', 
            slug=f'my-first-post-{x}', 
            author=u,# no se pone la x porque es el mismo siempre
            content=f'My first post content {x}')
        
    def test_urls(self):
        '''
        Comprobar que la vista de lista de posts devuelve 20
        '''
        # pagina inicial
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) # 200 es el codigo de ok
        #admin
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302) # 200 es el codigo de ok
        #primer post
        p = Post.objects.first()
        slug = p.slug
        response = self.client.get(f'/{slug}/')
        self.assertEqual(response.status_code, 200) # 200 es el codigo de ok