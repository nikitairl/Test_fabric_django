from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('accounts/logout/', views.logout, name='logout'),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
