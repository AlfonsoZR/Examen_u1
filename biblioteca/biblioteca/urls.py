"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from django.contrib import admin
from libros.views import LibroDetailView, LibrosListView, LibrosUpdateView

from libros import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^libros/$', views.lista_libros, name='lista_libros'),

    url(r'^libros/lista$', LibrosListView.as_view(), name='lista_view'),
    url(r'^libros/(?P<pk>\d+)/$', LibroDetailView.as_view(), name='detalle_view'),
    url(r'^detalle/(?P<object_id>\d+)/actualizar/$', views.actualizar, name='actualizar'),

    url(r'^Libro/(?P<pk>\d+)/actualizar/$', LibrosUpdateView.as_view(), name='update_view'),


    url(r'^detalle/(?P<object_id>\d+)/$', views.detalle, name='detalle_libro'),
    url(r'^agregar/$', views.agregar_libro, name='agregar_libro'),


]
