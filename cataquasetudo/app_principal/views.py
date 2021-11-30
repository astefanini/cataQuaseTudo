from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.db.models import Q
from django.views.generic import CreateView
from app_principal.models import Cliente, Contrato, Prestador, Transporte
from app_principal.forms import TransporteCreateForm
from app_principal.forms import ContratoCreateForm


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ClienteListTodosView(ListView):
    template_name = "app_principal/cliente_list_todos.html"
    model = Cliente
    context_object_name = "cliente_list"

def ClienteListView(request, id_codigo):
    # Cria um objeto vazio chamado clientes
    cliente_list = None

    #Aplica o filtro sobre os objetos em Cliente
    v_cliente_filtrado = Cliente.objects.filter(codigo=id_codigo)

    # Verifica se foi encontrado algum registro
    if len(v_cliente_filtrado) > 0 :
        cliente_list = v_cliente_filtrado
    else:
        cliente_list = None

    # Retorna o template clientes_lista.html e passa o filtro como parâmetro
    return render(request, 'app_principal/cliente_list.html', {'cliente_list': cliente_list, })

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

def ContratoCreateView(request, id_cliente, id_transporte):
    form = ContratoCreateForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cliente_list_todos'))
    else:
       return render(request, "app_principal/contrato_create.html", {'form': form, 'id_cliente': id_cliente, 'id_transporte': id_transporte })

def ContratoClienteListView(request, id_cliente):
    # Cria um objeto vazio chamado transporte_list
    contrato_cliente_list = None

    #Aplica o filtro sobre os objetos em Transporte
    v_contrato_cliente_filtrado = Contrato.objects.filter(cliente=id_cliente)

    # Verifica se foi encontrado algum registro
    if len(v_contrato_cliente_filtrado) > 0 :
        contrato_cliente_list = v_contrato_cliente_filtrado
    else:
        contrato_cliente_list = None

    # Retorna o template transporte_lista.html e passa o filtro como parâmetro
    return render(request, 'app_principal/contrato_cliente_list.html', {'contrato_cliente_list': contrato_cliente_list})

def ContratoTransporteListView(request, id_veiculo):
    # Cria um objeto vazio chamado transporte_list
    transporte_list = None

    #Aplica o filtro sobre os objetos em Transporte
    v_transporte_filtrado = Transporte.objects.filter(codigo=id_veiculo)

    # Verifica se foi encontrado algum registro
    if len(v_transporte_filtrado) > 0 :
        transporte_list = v_transporte_filtrado
    else:
        transporte_list = None

    # Retorna o template transporte_lista.html e passa o filtro como parâmetro
    return render(request, 'app_principal/contrato_transporte_list.html', {'transporte_list': transporte_list})


class PrestadorListTodosView(ListView):
    template_name = "app_principal/prestador_list_todos.html"
    model = Prestador
    context_object_name = "prestador_list_todos"

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


def TransporteCreateView(request, id_prestador):
    form = TransporteCreateForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('prestador_list_todos'))
    else:
       return render(request, "app_principal/transporte_create.html", {'form': form, 'id_prestador': id_prestador})

def TransporteListView(request, id_prestador):
    # Cria um objeto vazio chamado transporte_list
    transporte_list = None

    #Aplica o filtro sobre os objetos em Transporte
    v_transporte_filtrado = Transporte.objects.filter(prestador=id_prestador)

    # Verifica se foi encontrado algum registro
    if len(v_transporte_filtrado) > 0 :
        transporte_list = v_transporte_filtrado
    else:
        transporte_list = None

    # Retorna o template transporte_lista.html e passa o filtro como parâmetro
    return render(request, 'app_principal/transporte_list.html', {'transporte_list': transporte_list})

def TransporteContratoListView(request, id_veiculo):
    # Cria um objeto vazio chamado transporte_list
    transporte_contrato_list = None

    #Aplica o filtro sobre os objetos em Transporte
    v_transporte_contrato_filtrado = Contrato.objects.filter(transporte_id=id_veiculo)

    # Verifica se foi encontrado algum registro
    if len(v_transporte_contrato_filtrado) > 0 :
        transporte_contrato_list = v_transporte_contrato_filtrado
    else:
        transporte_contrato_list = None

    # Retorna o template transporte_lista.html e passa o filtro como parâmetro
    return render(request, 'app_principal/transporte_contrato_list.html', {'transporte_contrato_list': transporte_contrato_list})

def TransporteListTodosView(request, id_cliente):
    # Cria um objeto vazio chamado transporte_list
    transporte_list = None

    #Aplica o filtro sobre os objetos em Transporte
    v_transporte_filtrado = Transporte.objects.all

    # Verifica se foi encontrado algum registro
    # if len(v_transporte_filtrado) > 0 :
    transporte_list = v_transporte_filtrado
    # else:
    # transporte_list = None

    # Retorna o template transporte_lista.html e passa o filtro como parâmetro
    return render(request, 'app_principal/transporte_list_todos.html', {'transporte_list': transporte_list, 'id_cliente': id_cliente})
