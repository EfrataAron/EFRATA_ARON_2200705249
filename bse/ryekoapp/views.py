from django.shortcuts import render
from .models import SoilMoistureReading
# Create your views here.

print("Loading ryekoapp/views.py")

def home_view(request):
    return render(request, 'home.html') 


def moisture_list_view(request):
    readings = SoilMoistureReading.objects.all().order_by('-timestamp')# descending order of timestamp
    return render(request, 'moisture_list.html', {'readings': readings})
