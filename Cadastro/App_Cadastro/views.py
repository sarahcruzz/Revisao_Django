from django.shortcuts import render
from .models import *

# Create your views here.
def abre_index(request):
    return render(request, 'index.html')

def cadastrarPessoa(request):
    if (request.method == 'POST'):
        nomeCadastro = request.POST.get('nome')
        idadeCadastro = request.POST.get('idade')

        gravaCadastro = Pessoa(
            nome = nomeCadastro,
            idade = idadeCadastro
        )

        gravaCadastro.save()
        print("Dados salvos no banco de dados")

        mensagem = f"Dados cadastrados \nNome: {nomeCadastro} \nIdade: {idadeCadastro}"

        pessoas = Pessoa.objects.all()
        print(f"Tudo de pessoa: {pessoas}")

        return render(request, 'index.html', {'mensagem': mensagem, 'pessoas': pessoas})
    
    