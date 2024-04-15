from django.urls import path


from .views import (
    Home,
    Categorydetails,
    productdetails,
    ProductList,
    SearchProducts,
    CheckOut,
    Contact,
    ShoppingCart,
)
urlpatterns = [ 
    path('', Home.as_view(), name='home'),
    path('productdetails/<str:slug>/', productdetails.as_view(), name='productdetails'),
    path('categorydetails/<str:slug>/', Categorydetails.as_view(), name='categorydetails'),
    path('productlist/', ProductList.as_view(), name='productlist'),
    path('search-products/', SearchProducts.as_view(), name='search-products'),
    path('CheckOut/', CheckOut.as_view(), name='CheckOut'),
    path('contact/', Contact.as_view(), name='contact'),
    path('shoppingcart/', ShoppingCart.as_view(), name='shoppingcart'),
   
]