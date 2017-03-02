from django.contrib import admin

# Register your models here.

from libros.models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","ISBN","autor","editorial","precio","nombre"]
    search_fields = ["autor","editorial"]
    list_editable = ["nombre","precio"]
    list_filter = ["nombre","precio"]

    class Meta:
        model = Libro

admin.site.register(Libro,LibroAdmin)
