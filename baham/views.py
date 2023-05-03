from django.template import loader
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from baham.enum_types import VehicleType
from baham.models import VehicleModel
from django.urls import reverse
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def view_home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))

def view_vehicles(request):
    print("============================================")
    print("TEST")
    template = loader.get_template("vehicles.html")
    vehicles = VehicleModel.objects.all().order_by("vendor")
    context = {
        "vehicles" : vehicles,
    }
    return HttpResponse(template.render(context, request))

def add_vehicles(request):
    template = loader.get_template("add_vehicles.html")
    vehicleTypes = [tag for tag in VehicleType]
    context = {
        "VehicleType" : vehicleTypes
    }
    return HttpResponse(template.render(context, request))

def edit_vehicles(request):
    template = loader.get_template("edit_vehicles.html")
    return HttpResponse(template.render({}, request))


def view_contacts(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))

def view_aboutus(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))


def save_vehicle(request):
    _vendor = request.POST.get('vendor')
    _model = request.POST.get('model')
    _capacity = request.POST.get('capacity')
    _type = request.POST.get('type')

    # user = User.objects.create_user(username='10618',email='noor@example.com',password='test123')
    # user.save()
    
    newModel = VehicleModel(vendor=_vendor, model=_model, type=_type, capacity=_capacity)
    newModel.save()
    return HttpResponseRedirect(reverse('ViewVehicles')
)


def delete_vehicle(request, pk):
    vehicle = get_object_or_404(VehicleModel, pk=pk)
    vehicle.delete()
    return redirect('ViewVehicles')