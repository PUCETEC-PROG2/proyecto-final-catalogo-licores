from django.urls import path
from . import views

app_name = 'liquorManagment'

urlpatterns = [
    path("", views.index, name="index"),

    # Categoria
    path("category/", views.categoryList, name="category"),
    path("add_category/", views.addCategory, name='add_category'),
    path("category/category_detail/<int:id_category>/", views.categoryDetail, name="category_detail"),
    path("category/edit_category/<int:id_category>/", views.editCategory, name='edit_category'),
    path("category/remove_category/<int:id_category>/", views.removeCategory, name='remove_category'),

    # Productoss
    path("product/", views.productList, name="product"),
    path("add_product/", views.addProduct, name='add_product'),
    path("product/product_detail/<int:id_product>/", views.productDetail, name="product_detail"),
    path("product/edit_product/<int:id_product>/", views.editProduct, name='edit_product'),
    path("product/remove_product/<int:id_product>/", views.removeProduct, name='remove_product'),

    # Cliente
    path("client/", views.clientList, name="client"),
    path("add_client/", views.addClient, name='add_client'),
    path("client/client_detail/<int:id_client>/", views.clientDetail, name="client_detail"),
    path("client/edit_client/<int:id_client>/", views.editClient, name='edit_client'),
    path("client/remove_client/<int:id_client>/", views.removeClient, name='remove_client'),

    # Compra
    path("orderList/", views.orderList, name="orderList"),
    path("add_order/", views.addOrder, name='add_order'),
    path("orderList/orderDetail/<int:id_purchase_order>/", views.orderDetail, name="orderDetail"),

    #Login

    path("login/", views.CustomLoginView.as_view(), name='login'),

]
