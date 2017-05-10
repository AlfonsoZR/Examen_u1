from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from biblioteca.mixinslug import MixinSlug




from .models import Libro
from .forms import LibroAddForm, LibrosModelForm

# Create your views here.
def home(request):
    #Logico de negocio alias hechizo
    m = "Hola Biblioteca"
    contexto= {"mensaje":m}
    return render(request, 'home.html', contexto)

def lista_libros(request):
    consulta = Libro.objects.all()
    print request
    m = "consulta de libros"
    template = "listaDeLibros.html"
    contexto = {"mensaje":m,
                "consulta":consulta}
    return render(request, template, contexto)

def detalle(request, object_id=None):
    #Logico de negocio alias hechizo
    libro = get_object_or_404(Libro, id=object_id)
    m = "libro nuevo"
    template = "detalleLibro.html"
    contexto= {"mensaje":m,
           "libro": libro }
    return render(request, template, contexto)


def agregar_libro(request):
    form = LibroAddForm(request.POST or None)
    if request.POST == "POST":
        print request.POST
    if form.is_valid():

        data = form.cleaned_data
        nombre = data.get("nombre")
        autor = data.get("autor")
        editorial = data.get("editorial")
        ISBN = data.get("ISBN")
        precio = data.get("precio")



        nuevo_libro = Libro()
        nuevo_libro.nombre = nombre
        nuevo_libro.autor = autor
        nuevo_libro.esditorial = editorial
        nuevo_libro.ISBN = ISBN
        nuevo_libro.precio = precio
        nuevo_libro.save()

    template = "agregar_libro.html"
    context = {"form":form}
    return render(request,template,context)











#examen unidad 2
def actualizar(request, object_id=None):
    #Logico de negocio alias hechizo
    libros = get_object_or_404(Libro, id=object_id)
    form = LibrosModelForm(request.POST or None, instance=libros)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "actualizar.html"
    contexto= {
           "libro": libros,
           "form":form,
           "titulo":"Actualizar Libro"
           }
    return render(request, template, contexto)



#examen unidad 3 (vistas basadas en clases)
class LibrosCreateView(CreateView):
    model = Libro
#   template_name = "form.html"
    form_class = LibrosModelForm
    #success_url = "/producto/crear/"

    def get_context_data(self, *args, **kwargs):
        context = super(LibrosCreateView, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Guardar"
        return context


class LibrosUpdateView(UpdateView):
    model = Libro
#    template_name = "form.html"
    form_class = LibrosModelForm
    success_url = "/libros/lista/"

    def get_context_data(self, *args, **kwargs):
        context = super(LibrosUpdateView, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Editar"
        return context

class LibrosDetailView(DetailView, MixinSlug):
    model = Libro
    # def get_object(self, *args, **kwargs):
    #       print self.kwargs
    #       slug = self.kwargs.get("slug")
    #       print slug
    #       ModelClass = self.model
    #       if slug is not None:
    #           try:
    #               #producto = get_object_or_404(Producto, slug=slug)
    #               obj = get_object_or_404(ModelClass, slug=slug)
    #           except:
    #               #producto = Producto.objects.filter(slug=slug).order_by("-nombre").first()
    #               obj = ModelClass.objects.filter(slug=slug).order_by("-nombre").first()
    #       else:
    #           obj = super(LibrosDetailView, self).get_object(*args, **kwargs)
    #
    #       return obj

class LibrosListView(ListView):
    model = Libro

    def get_queryset(self, *args, **kwargs):
        qs = super(LibrosListView, self).get_queryset(**kwargs)
        return qs
