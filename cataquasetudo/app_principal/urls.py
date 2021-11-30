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
    path('cliente_list/<int:id_codigo>', views.ClienteListView, name = 'cliente_list'),
    path('cliente_create', ClienteCreateView.as_view(), name = 'cliente_create'),    
    path('contrato_create/<int:id_cliente>/<int:id_transporte>', views.ContratoCreateView, name = 'contrato_create'),            
    path('contrato_cliente_list/<int:id_cliente>', views.ContratoClienteListView, name = 'contrato_cliente_list'),            
    path('contrato_transporte_list/<int:id_veiculo>', views.ContratoTransporteListView, name = 'contrato_transporte_list'),                
    path('prestador_list_todos', PrestadorListTodosView.as_view(), name = 'prestador_list_todos'),    
    path('prestador_list/<int:id_codigo>', views.ClienteListView, name = 'cliente_list'),    
    path('prestador_create', PrestadorCreateView.as_view(), name = 'prestador_create'),
    path('prestador_login', TemplateView.as_view(template_name="app_principal/prestador_login.html")),
    path('transporte_create/<int:id_prestador>', views.TransporteCreateView, name = 'transporte_create'),
    path('transporte_list/<str:id_prestador>', views.TransporteListView, name = 'transporte_list'),
    path('transporte_list_todos/<str:id_cliente>', views.TransporteListTodosView, name = 'transporte_list_todos'),    
    path('transporte_contrato_list/<str:id_veiculo>', views.TransporteContratoListView, name = 'transporte_contrato_list'),    
]

