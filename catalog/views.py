from django.shortcuts import render

from catalog.models import Category


# Create your views here.


def index(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
    return render(request, 'catalog/contact.html')
