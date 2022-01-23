from django.shortcuts import render
from product.models import Product
import sys
sys.path.append("/Users/zhangweibin/gitproject/learngit/autotest")
from autotest.Log_method import Logger

loger = Logger("product-proviews")


# Create your views here.
def product_manage(request):
    username = request.session.get('user', '')
    product_list = Product.objects.all()
    return render(request, "product_manage.html", {'user': username, 'products': product_list})