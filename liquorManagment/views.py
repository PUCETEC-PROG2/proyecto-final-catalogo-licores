from django.shortcuts import render,get_list_or_404, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.template import loader
from .models import Category, Product,Client,Purchase_order,Order_item
from liquorManagment.forms import CategoryForm,ProductForm,ClientForm,PurchaseOrderForm,OrderItemForm, OrderItemFormSet

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Crud Category

def categoryList(request):
    category = Category.objects.all()
    context = {
        'Category': category
    }
    return render(request, 'categorias.html', context)

def categoryDetail(request, id_category):
    category= get_object_or_404(Category, pk=id_category)
    template = loader.get_template('categoria_details.html')
    context = {
        'Category': category
    }
    return HttpResponse(template.render(context, request))

@login_required
def addCategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liquorManagment:category')
    else:
        form = CategoryForm()
    return render(request, 'categoria_form.html', {'form': form})

@login_required
def editCategory(request, id_category):
    category = get_object_or_404(Category, pk=id_category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('liquorManagment:category')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categoria_form.html', {'form': form})

@login_required
def removeCategory(request, id_category):
    category = get_object_or_404(Category, pk=id_category)
    category.delete()
    return redirect('liquorManagment:category')

# Crud Products

def productList(request):
    product = Product.objects.all()
    context = {
        'Product': product
    }
    return render(request, 'productos.html', context)

def productDetail(request, id_product):
    product= get_object_or_404(Product, pk=id_product)
    template = loader.get_template('producto_details.html')
    context = {
        'Product': product
    }
    return HttpResponse(template.render(context, request))

@login_required
def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Pendiente modificar
            return redirect('liquorManagment:product')
    else:
        form = ProductForm()
        # Pendiente modificar      
    return render(request, 'producto_form.html', {'form': form})

@login_required
def editProduct(request, id_product):
    product = get_object_or_404(Product, pk=id_product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            # Pendiente modificar
            return redirect('liquorManagment:product')
    else:
        form = ProductForm(instance=product)
        # Pendiente modificar
    return render(request, 'producto_form.html', {'form': form})

@login_required
def removeProduct(request, id_product):
    product = get_object_or_404(Product, pk=id_product)
    product.delete()
    return redirect('liquorManagment:product')

# Crud Clients
def clientList(request):
    client = Client.objects.all()
    context = {
        'Client': client
    }
    # Pendiente Modificar
    return render(request, 'clientes.html', context)

def clientDetail(request, id_client):
    client = get_object_or_404(Client, pk=id_client)
    # Pendiente Modificar
    template = loader.get_template('cliente_details.html')
    context = {
        'Client': client
    }
    return HttpResponse(template.render(context, request))

@login_required
def addClient(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            # Pendiente modificar
            return redirect('liquorManagment:client')
    else:
        form = ClientForm()
    # Pendiente modificar      
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def editClient(request, id_client):
    client = get_object_or_404(Client, pk=id_client)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('liquorManagment:client')
    else:
        form = ClientForm(instance=client)
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def removeClient(request, id_client):
    client = get_object_or_404(Client, pk=id_client)
    client.delete()
    return redirect('liquorManagment:client')

# Crud Purchase Order
def orderList(request):
    order = Purchase_order.objects.all()
    context = {
        'Order': order
    }
    return render(request, 'compras.html', context)

def orderDetail(request, id_purchase_order):
    order = get_object_or_404(Purchase_order, pk=id_purchase_order)
    template = loader.get_template('compra_details.html')
    context = {
        'Order': order
    }
    return HttpResponse(template.render(context, request))

@login_required
def addItem(request):
    if request.method == "POST":
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LiquorManagment:index')
    else:
        form = OrderItemForm()

    return render(request, 'index.html', {'form': form})

@login_required

def addOrder(request):
    if request.method == 'POST':
        purchase_order_form = PurchaseOrderForm(request.POST)
        order_item_formset = OrderItemFormSet(request.POST, prefix='order_items')

        if purchase_order_form.is_valid() and order_item_formset.is_valid():
            purchase_order = purchase_order_form.save(commit=False)
            purchase_order.total_price = 0  # Inicializa el precio total en 0

            purchase_order.save()  # Guarda la orden de compra

            for form in order_item_formset:
                order_item = form.save(commit=False)
                order_item.purchase_order_id_fk = purchase_order
                order_item.save()
                purchase_order.total_price += order_item.product_id_fk.price * order_item.quantity

            purchase_order.save()  # Guarda el precio total actualizado

            return redirect('liquorManagment:orderList')  # Redirige a la lista de órdenes de compra después de guardar

    else:
        purchase_order_form = PurchaseOrderForm()
        order_item_formset = OrderItemFormSet(prefix='order_items')

    return render(request, 'compra_form.html', {
        'purchase_order_form': purchase_order_form,
        'order_item_formset': order_item_formset,
    })
#Login
class CustomLoginView(LoginView):
    template_name = 'login.html'

