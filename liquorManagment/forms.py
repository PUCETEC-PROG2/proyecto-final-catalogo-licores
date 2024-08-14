from django import forms
from .models import Category, Product, Client, Purchase_order, Order_item

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

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model= Purchase_order
        fields = ['id_client_fk','order_date','total_price']
        widgets={
            'id_client_fk': forms.Select(attrs={'class':'form-control','placeholder':'Ingrese el ID'}),
            'order_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre'}),
            'total_price': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el Apellido'}),
        }
        labels={
            'id_client_fk': 'Cliente',
            'order_date': 'Fecha Orden',
            'total_price': 'Precio Total',
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model= Order_item
        fields = ['purchase_order_id_fk','product_id_fk','quantity']
        widgets={
            'purchase_order_id_fk': forms.NumberInput(attrs={'class':'form-control'}),
            'product_id_fk': forms.NumberInput(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels={
            'purchase_order_id_fk': 'Orden de Compra',
            'product_id_fk': 'Producto',
            'quantity': 'Cantidad',
        }
        
                                                                                                       


