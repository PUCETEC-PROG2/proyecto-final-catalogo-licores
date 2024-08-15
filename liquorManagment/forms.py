from django import forms
from .models import Category, Product, Client, Purchase_order, Order_item
from django.forms import inlineformset_factory

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields = ['category_name']
        widgets={
            'category_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Categoria'}),
        }
        labels={
            'category_name': 'Nombre Categoria',
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ['product_name', 'price', 'product_image','is_active','available_stock','Category_id_fk']
        widgets={
            'product_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'}),
            'price': forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el precio'}),
            'product_image': forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Subir Imagen'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'available_stock': forms.NumberInput(attrs={'class':'form-control','placeholder':'Unidades disponibles'}),
            'Category_id_fk': forms.Select(attrs={'class':'form-control'}),
        }
        labels={
            'product_name': 'Nombre Producto',
            'price': 'Precio',
            'product_image': 'Imagen',
            'is_active': 'Activo',
            'available_stock': 'Stock Disponible',
            'Category_id_fk': 'Categoria'
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model= Client
        fields = ['identification','name','last_name','phone', 'email']
        widgets={
            'identification': forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el ID'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el Apellido'}),
            'phone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese el telefono'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'example@example.com'}),
        }
        labels={
            'identification': 'Identificación',
            'name': 'Nombre',
            'last_name': 'Apellido',
            'phone': 'Telefono',
            'email': 'Correo',
        }

class OrderItemForm(forms.ModelForm):
    price = forms.DecimalField(
        max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': True})
    )

    class Meta:
        model = Order_item
        fields = ['product_id_fk', 'quantity', 'price']
        widgets = {
            'product_id_fk': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'onchange': 'calculateFinalPrice(this)'}),
        }
        labels = {
            'product_id_fk': 'Producto',
            'quantity': 'Cantidad',
            'price': 'Precio Unitario',
        }

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = Purchase_order
        fields = ['id_client_fk', 'order_date', 'total_price']
        widgets = {
            'id_client_fk': forms.Select(attrs={'class': 'form-control'}),
            'order_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
        }
        labels = {
            'id_client_fk': 'Cliente',
            'order_date': 'Fecha Orden',
            'total_price': 'Precio Total',
        }

    def __init__(self, *args, **kwargs):
        super(PurchaseOrderForm, self).__init__(*args, **kwargs)
        self.fields['id_client_fk'].queryset = Client.objects.all()  # Asegúrate de que los clientes estén disponibles

OrderItemFormSet = inlineformset_factory(
    Purchase_order,  # Modelo principal
    Order_item,      # Modelo del formset
    form=OrderItemForm,  # Formulario
    extra=1,         # Número de formularios vacíos iniciales
    can_delete=True  # Permitir eliminar formularios
)