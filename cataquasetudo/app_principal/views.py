from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic import CreateView
from app_principal.models import Cliente, Contrato, Prestador, Transporte


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ClienteListTodosView(ListView):
    template_name = "app_principal/cliente_list.html"
    model = Cliente
    context_object_name = "cliente_list"

def ClienteListView(request, id_usuario, id_senha):
    # Cria um objeto vazio chamado clientes
    cliente_list = None

    #Aplica o filtro sobre os objetos em Cliente
    v_cliente_filtrado = Cliente.objects.filter(usuario=id_usuario, senha=id_senha)

    # Verifica se foi encontrado algum registro
    if len(v_cliente_filtrado) > 0 :
        cliente_list = v_cliente_filtrado
    else:
        cliente_list = None

    # Retorna o template clientes_lista.html e passa o filtro como parâmetro
    return render(request, 'app_principal/cliente_list.html', {'cliente_list': cliente_list})

class ClienteCreateView(CreateView):
    template_name = "app_principal/cliente_create.html"
    model = Cliente
    fields = [
            'nome',
            'rg',
            'cpf',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'cep',
            'usuario',
            'senha'
             ]
    exclude = [
            'codigo'
            ]
    success_url = reverse_lazy("cliente_list_todos")

def cliente_login(request):
    id_usuario = request.POST.get('id_usuario')
    id_senha = request.POST.get('id_senha')    
    context={'id_usuario':id_usuario, 'id_senha':id_senha}
    return render(request, 'app_principal/cliente_login.html', context=context)

class ContratoCreateView(CreateView):
    template_name = "app_principal/contrato_create.html"
    model = Contrato
    fields = [
            'cliente',
            'transporte',
            'quantidade',
            'moveis',
            'eletro',
            'metais',
            'alvenaria',
            'madeiramento',
            'troncos',
            'arbusto',
            'grama'
             ]
    exclude = [
            'codigo'
            ]

    success_url = reverse_lazy("contrato_create")

class PrestadorListTodosView(ListView):
    template_name = "app_principal/prestador_list.html"
    model = Prestador
    context_object_name = "prestador_list"

def PrestadorListView(request, id_usuario, id_senha):
    # Cria um objeto vazio chamado clientes
    prestador_list = None

    #Aplica o filtro sobre os objetos em Cliente
    v_prestador_filtrado = Prestador.objects.filter(usuario=id_usuario, senha=id_senha)

    # Verifica se foi encontrado algum registro
    if len(v_prestador_filtrado) > 0 :
        prestador_list = v_prestador_filtrado
    else:
        prestador_list = None

    # Retorna o template clientes_lista.html e passa o filtro como parâmetro
    return render(request, 'app_principal/prestador_list.html', {'prestador_list': prestador_list})


class PrestadorCreateView(CreateView):
    template_name = "app_principal/prestador_create.html"
    model = Prestador
    fields = [
            'nome',
            'insc_est',
            'cnpj',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'cep',
            'usuario',
            'senha'
             ]
    exclude = [
            'codigo'
            ]

    success_url = reverse_lazy("prestador_list_todos")

class TransporteCreateView(CreateView):
    template_name = "app_principal/transporte_create.html"
    model = Transporte
    fields = [
            'prestador',
            'veiculo',
            'capacidade',
            'moveis',
            'eletro',
            'metais',
            'alvenaria',
            'madeiramento',
            'troncos',
            'arbusto',
            'grama',
            'preco'
             ]
    exclude = [
            'codigo'
            ]

    success_url = reverse_lazy("contrato_create")

