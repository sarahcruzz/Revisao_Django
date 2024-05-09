from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.abre_index, name='abre_index'),
    path('', views.cadastrarPessoa, name='cadastrarPessoa'),
    path('editarinfo/<int:id>', views.editarInfo, name='editarInfo'),
    path('excluirPessoa/<int:id>', views.excluirPessoa, name='excluir')
]