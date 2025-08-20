from django.urls import path

from . import views as goods

app_name = 'goods'

urlpatterns = [
    path('',goods.catalog,name='index'),
    path('product/<slug:product_slug>/',goods.product,name='product'), 
]