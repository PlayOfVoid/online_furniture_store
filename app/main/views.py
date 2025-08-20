from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories
# Create your views here.


def index(request) -> HttpResponse:
    categories = Categories.objects.all()
    
    context = {
        'title':'Home - Главная',
        'categories':categories,
        
    }
    return render(request,'main/index.html',context)


def about(request) -> HttpResponse:
    context = {
        'title':'Home - О нас',
        'content': ' О нас',
        'text_on_page':'Текс о том почему этот магазин такой классный, и какой хороший товар.'
        
    }
    
    return render(request,'main/about.html',context)