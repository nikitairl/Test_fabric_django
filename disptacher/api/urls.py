from django.urls import path

from . import views


urlpatterns = [
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
