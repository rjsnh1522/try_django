from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.



def product_list_view(request):
    query_set = Product.objects.all()
    context = {
        "object_list" : query_set
    }
    return render(request, "products/all_products.html", context)

def delete_product(request, id):
    print(id)
    obj =  get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../create')
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context) 


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj =  get_object_or_404(Product, id=id)
    # import ipdb; ipdb.set_trace()
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }

    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form" : my_form
    }
    return render(request, "products/product_create.html",context)

def product_update_view(request, id):
    # import ipdb; ipdb.set_trace()
    if request.method == "GET":
        obj = get_object_or_404(Product, id=id)
    # if request.method == "POST":

    context = {
        "object": obj
    }

    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     context = {}
#     return render(request, "products/product_create.html",context)



# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form' : form
#     }
#     return render(request, "products/product_create.html",context)

def product_detail_view(request):
    # obj = Product.objects.get(id=1)
    # import ipdb; ipdb.set_trace()
    # context = {
    #     'title' : obj.title,
    #     'description': obj.description
    # }
    context = {
        "object" : 'obj'
    }
    return render(request, "products/product_detail.html", context)