from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .ml_model import predict_price
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@login_required(login_url='login')
def index(request):
    properties = Property.objects.all()
    return render(request, 'properties/index.html', {'properties': properties})

@login_required(login_url='login')
def add_property(request):
    if request.method == "POST":
        name = request.POST.get("name")
        lat = request.POST.get("latitude")
        lng = request.POST.get("longitude")
        area = request.POST.get("area")
        price = request.POST.get("price")

        Property.objects.create(
            name=name,
            latitude=lat,
            longitude=lng,
            area=area,
            price=price
        )
        return redirect('home')

    return render(request, 'properties/add.html')

def delete_property(request, id):
    prop = get_object_or_404(Property, id=id)
    prop.delete()
    return redirect('home')

def predict(request):
    try:
        area = float(request.GET.get("area", 0))
        lat = float(request.GET.get("lat", 0))
        lng = float(request.GET.get("lng", 0))

        price = predict_price(area, lat, lng)

        return JsonResponse({"price": price})

    except Exception as e:
        return JsonResponse({"error": str(e)})
    
def signup_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(request, "Account created successfully")

        return redirect("login")

    return render(request, "properties/signup.html")

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "properties/login.html")

def logout_view(request):

    logout(request)

    return redirect("login")    