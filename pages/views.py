from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "this is my context",
        "my_number" : 123423,
        "my_list": [1, 23, 4, 5, 67, 3],
        "html" :"<h1>Hello World</h1>"
    }
    # import ipdb; ipdb.set_trace()
    return render(request, "contact.html", my_context)
