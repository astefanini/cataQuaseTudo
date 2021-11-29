from django.urls import path
from django.views.generic import TemplateView
from . import views
from app_principal.views import ClienteListTodosView
from app_principal.views import ClienteCreateView

from app_principal.views import ContratoCreateView

from app_principal.views import PrestadorListTodosView
from app_principal.views import PrestadorCreateView

from app_principal.views import TransporteCreateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="app_principal/index.html")),
    path('cliente_list_todos', ClienteListTodosView.as_view(), name = 'cliente_list_todos'),
    path('cliente_list/<str:id_usuario>/<str:id_senha>', views.ClienteListView, name = 'cliente_list'),
    path('cliente_create', ClienteCreateView.as_view(), name = 'cliente_create'),    
    # path('cliente_login/<str:id_usuario>/<str:id_senha>',  views.cliente_login, name="cliente_login"),
    path('cliente_login',  views.cliente_login, name="cliente_login"),    

    path('contrato_create', ContratoCreateView.as_view(), name = 'contrato_create'),        

    path('prestador_list_todos', PrestadorListTodosView.as_view(), name = 'prestador_list_todos'),    
    path('prestador_list/<str:id_usuario>/<str:id_senha>', views.ClienteListView, name = 'cliente_list'),    
    path('prestador_create', PrestadorCreateView.as_view(), name = 'prestador_create'),
    path('prestador_login', TemplateView.as_view(template_name="app_principal/prestador_login.html")),
    path('prestador_list/<str:id_usuario>/<str:id_senha>', views.PrestadorListView, name = 'prestador_list'),    
    
    path('transporte_create', TransporteCreateView.as_view(), name = 'transporte_create'),    
]

