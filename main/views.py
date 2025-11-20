from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Product, Owner
from django.urls import reverse
from .forms import OwnerForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def index(request):
    if request.method == "POST":
        owner = OwnerForm(request.POST, request.FILES)
        if owner.is_valid():
            owner.save()
            print(f"Saved owner: {owner.cleaned_data['full_name']}")
        else:
            print(f"Form errors: {owner.errors}")
        return redirect(reverse('main:index_page', args=()))

    products = Product.objects.all()
    product2 = Product.objects.first()  
    owners = Owner.objects.all()

    return render(request, "main/index.html", {
        "owners": owners,
        "product2": product2,
        "products": products
    })


def header(request):
    product3 = Product.objects.all()  # Показываем ВСЕ продукты
    return render(request, "main/header.html", {"product3": product3})

def detail(request, id):
    owner = Owner.objects.get(pk=id)
    return render(request, "main/detail.html", {"owner": owner})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("main:profile_page"))
        else:
            return redirect(reverse("main:login_page"))
        
    return render(request, "main/login.html", {})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        email = request.POST.get("email", None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name)
        
        return redirect(reverse("main:login_page"), args=())


    return render(request, "main/register.html", {})

def profile(request):
    if request.user.is_authenticated:
        owners_count = Owner.objects.count()
        products_count = Product.objects.count()
        
        return render(request, "main/profile.html", {
            "owners_count": owners_count,
            "products_count": products_count,
        })
    else: 
        return redirect(reverse("main:login_page"))


def logout_view(request):
    logout((request))
    return redirect(reverse("main:login_page"), args=())



# class MyTemplateView(TemplateView):
#     template_name = "main/c_based_template.html"

#     def get_context_data(self, **kwargs):
    
#         return {}
