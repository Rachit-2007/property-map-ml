from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .ml_model import predict_price
from django.http import JsonResponse

def index(request):
    properties = Property.objects.all()
    return render(request, 'properties/index.html', {'properties': properties})

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