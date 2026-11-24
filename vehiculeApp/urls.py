from django.urls import path
from . import views

app_name = "VehiculeApp"

urlpatterns = [
    path("", views.VehiculeListView.as_view(), name="list"),
    path("create/", views.VehiculeCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.VehiculeUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.VehiculeDeleteView.as_view(), name="delete"),
]
