from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product



def index (request):
    products = Product.objects.all()
    return render(request, "index.html",{'product' : products})



class SearchResultsView(ListView):
        model = Product
        template_name = 'search_results.html'

        def get_queryset(self):
            query = self.request.GET.get('q')
            object_list = Product.objects.filter(Q(name__icontains=query))
            return object_list


