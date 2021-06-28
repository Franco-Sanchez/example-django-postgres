from django.shortcuts import render
from testDB.models import Car, Driver

# Create your views here.

def car_detail(request, pk):

  owner_object = Driver.objects.get(pk=pk)
  car_objs = Car.objects.filter(owner_id=owner_object.id)
  context = {
    "vehicles": car_objs,
    "driver": owner_object
  }

  return render(request, "car_detail.html", context)