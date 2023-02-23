from django.urls import path
from . import views



urlpatterns = [
    path('',views.list_all, name='list_all'),
    path('<int:pk>',views.view_product,name='views_product'),
    path('create_product',views.create_product,name='create_product'),
    path('update/<int:pk>',views.updated_product,name='updated_product'),
    path('delete/<int:pk>',views.delete_product,name='deleted_product'),
]
