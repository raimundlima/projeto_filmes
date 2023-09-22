from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    
    GENERO_CHOICES = (
            ('acao' , 'Ação'),
            ('comedia' , 'Comédia'),
            ('ficcao' , 'Ficção'),
            ('terror' , 'Terror'),
            ('suspense' , 'Suspense'),
        )
    genero = forms.ChoiceField(choices= GENERO_CHOICES, label='Gênero')
    
    
    
    
    class Meta:
        model = Filme
        fields = ['id_filme', 'nome', 'genero', 'ano_lancamento', 'Sinopse', 'capa']

   

    
        

        
      


