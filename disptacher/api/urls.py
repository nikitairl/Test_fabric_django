from django.urls import path

from . import views


urlpatterns = [
    path('v1/dispatch/', views.DispatchViewSet.as_view(
        {'get': 'list', 'post': 'create'}),
        name='dispatch'),
    path('v1/dispatch/<int:pk>', views.DispatchViewSet.as_view(
        {'delete': 'delete', 'patch': 'patch'}),
    )

]
