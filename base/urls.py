from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns=[
    path('',views.getRoutes,name="routes"),
    path('products/',views.getProducts,name="products"),
    path('products/<str:pk>',views.getProduct,name="product"),
]