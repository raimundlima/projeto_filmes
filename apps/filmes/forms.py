from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    
    GENERO_CHOICES = (
            ('Ação' , 'Ação'),
            ('Comedia' , 'Comédia'),
            ('Ficção' , 'Ficção'),
            ('Terror' , 'Terror'),
            ('Suspense' , 'Suspense'),
            ('Drama' , 'Drama'),
        )
    genero = forms.ChoiceField(
        choices= GENERO_CHOICES, label='Gênero',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    
    nome = forms.CharField(
        label="Nome",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    ano_lancamento = forms.CharField(
        label="Ano Lanamento:",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


    Sinopse = forms.CharField(
        label="Sinopse:",
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )


    capa = forms.CharField(
        label="Capa:",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )



    
    
    class Meta:
        model = Filme
        fields = ['id_filme', 'nome', 'genero', 'ano_lancamento', 'Sinopse', 'capa']

   

    
        

        
      


