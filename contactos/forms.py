import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Carlos',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; margin-top: 5px;'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Yáñez',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; margin-top: 5px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: ejemplo@correo.com',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; margin-top: 5px;'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: +56912345678 o 912345678',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; margin-top: 5px;'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Av. Principal 123',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; margin-top: 5px;'
            }),
        }

    # Validar Correo Electrónico
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower().strip()
            
            # Verificar formato general de correo
            patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(patron_email, email):
                raise ValidationError("Ingresa un correo electrónico válido (ejemplo: usuario@dominio.com).")

            # Verificar si el correo ya está registrado por otro contacto
            query = Contacto.objects.filter(email=email)
            if self.instance and self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
            
            if query.exists():
                raise ValidationError("Este correo electrónico ya se encuentra registrado.")

        return email

    # Validar Teléfono 
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono:
            # Eliminar espacios en blanco
            telefono = telefono.strip().replace(" ", "")

            
            patron_telefono = r'^(\+?56)?(\d{9})$'
            
            if not re.match(patron_telefono, telefono):
                raise ValidationError("El teléfono debe tener un formato válido (Ej: +56912345678 o 912345678).")

        return telefono