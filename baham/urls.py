from django.urls import path,include

from . import views

urlpatterns = [
    path("", views.view_home, name="Home"),
    path("view_vehicles", views.view_vehicles, name="ViewVehicles"),
    path("add_vehicles", views.add_vehicles, name="AddVehicles"),
    path("edit_vehicles", views.add_vehicles, name="EditVehicles"),
    path("contact-us", views.view_contacts, name="ContactUs"),
    path("about-us", views.view_aboutus, name="AboutUs"),
    path("add_vehicles/SaveVehicle", views.save_vehicle, name="save-vehicle"),
    path('vehicles/<int:pk>/delete/', views.delete_vehicle, name='delete_vehicle')

]
