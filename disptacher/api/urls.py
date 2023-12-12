from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Fabric Dispatch API",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('v1/docs/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('v1/dispatch/', views.DispatchViewSet.as_view(
        {'get': 'list', 'post': 'create'}),
         name='dispatch'),
    path('v1/dispatch/<int:pk>', views.DispatchViewSet.as_view(
        {'delete': 'delete', 'patch': 'patch', 'get': 'retrieve'}),
         name='dispatch_direct'),
    path('v1/client/', views.ClientViewSet.as_view(
        {'get': 'list', 'post': 'create'}),
         name='client'),
    path('v1/client/<int:pk>', views.ClientViewSet.as_view(
        {'delete': 'delete', 'patch': 'patch', 'get': 'retrieve'}),
         name='client_direct'),
    path('v1/message/', views.MessageViewSet.as_view(
        {'get': 'list'}),
         name='message'),
    path('v1/message/<int:pk>', views.MessageViewSet.as_view(
        {'get': 'retrieve'}),
         name='message_direct'),
]
