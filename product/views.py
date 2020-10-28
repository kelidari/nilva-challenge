from django.db.models.query_utils import Q
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from django.contrib.auth.decorators import login_required
from . import forms


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'product': products})



def SearchResultsView(request):
    query = request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query))
    return render(request, "index.html", {'product': products})



@csrf_exempt
def BoughterPanel(request):
    # TODO check validation request
    context = {}
    context['product'] = request.GET['name']
    return render(request, 'order.html', context)


@login_required(login_url='accounts:login')
def create_product(request):
    if request.method == 'POST':
        form= forms.CreateProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:list')
    else:
        form = forms.CreateProduct()
    return render(request, 'create_product.html',{'form':form})
