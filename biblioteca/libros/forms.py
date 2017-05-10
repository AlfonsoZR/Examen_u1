from django import forms

from .models import Libro

OPCIONES_TIPO = (
    ('foto', "Foto"),
    ('video juego', "Video Juego"),
    ('libro', "Libro"),
)
class LibroAddForm(forms.Form):
	nombre  = forms.CharField(label="cual es el nombre del libro?", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de libro'}))
	autor = forms.CharField(label="cual es el nombre del autor?", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre del autor del libro'}))
	editorial = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	ISBN = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	precio = forms.DecimalField()

def clean_precio(self):
	precio = self.cleaned_data.get("precio")
	if precio <=200.00:
		raise forms.validationError("El precio minimo es de $200.00")
	elif precio >= 19999.00:
		raise forms.validationError("El precio maximo es de $19999.00")
	else:
		return precio

class LibrosModelForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=OPCIONES_TIPO)
    class Meta:
        model = Libro
        fields =[
            "nombre",
            "autor",
            "editorial",
			"precio"
        ]
        labels = {
            "nombre": "Cual es nombre del libro",
            "autor":"Nombre del autor del libro",
            "editorial":"editorial del libro",
			"precio":"Precio del libro"
        }
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ponga el nombre'}),
            "autor": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ponga el nombre del autor del libor'}),
            "editorial": forms.TextInput(attrs={'class': 'form-control'}),
			"precio": forms.NumberInput(attrs={'class': 'form-control'}),

        }

    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio <= 200.00:
            raise forms.ValidationError("El precio debe ser mayor que $100.00")
        elif precio >= 19999.00:
            raise forms.ValidationError("El precio debe ser menos que $19999.00")
        else:
            return precio
