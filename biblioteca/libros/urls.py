
from django.conf.urls import url
from django.contrib import admin

from libros.views import LibrosCreateView, LibrosUpdateView, LibrosDetailView, LibrosListView

from libros import views

urlpatterns = [
        url(r'^lista/$', LibrosListView.as_view(), name='libro_list'),
        url(r'^(?P<pk>\d+)/$', LibrosDetailView.as_view(), name='libro_detail'),
        url(r'^crear/$', LibrosCreateView.as_view(), name='crear_view'),

        url(r'^(?P<pk>\d+)/actualizar/$', LibrosUpdateView.as_view(), name='update_view'),
        url(r'^(?P<slug>[\w-]+)/$', LibrosDetailView.as_view(), name='detalle_slug'),

]
