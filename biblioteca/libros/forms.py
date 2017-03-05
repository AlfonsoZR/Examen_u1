from django import forms

class LibroAddForm(forms.Form):
	nombre  = forms.CharField()
	autor = forms.CharField()
	editorial = forms.CharField()
	ISBN = forms.CharField()
	precio = forms.DecimalField()

def clean_precio(self):
		precio = self.cleaned_data.get("precio")
		if precio <=200.00:
			raise forms.validationError("El precio minimo es de $200.00")
		elif precio >= 19999.00:
			raise forms.validationError("El precio maximo es de $19999.00")
		else:
			return
