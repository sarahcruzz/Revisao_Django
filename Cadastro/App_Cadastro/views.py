from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import *

# Create your views here.
# def abre_index(request):
#     return render(request, 'index.html')

def cadastrarPessoa(request):
    mensagem = ''
    pessoas = Pessoa.objects.all()
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
    
def excluirPessoa(request, id):
    print("cheguei aqui")
    pessoa = Pessoa.objects.get(pk=id)
    pessoa.delete()
   
    return HttpResponseRedirect(reverse("cadastrarPessoa"))
 
def editarInfo(request,id):
    pessoa = Pessoa.objects.get(pk=id)
    if(request.method == 'POST'):
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
       
        pessoa.nome = nome
        pessoa.idade = idade
       
        pessoa.save()
       
        return HttpResponseRedirect(reverse("cadastrarPessoa"))
   
    return render(request, 'edicao.html', {'pessoa':pessoa})
    