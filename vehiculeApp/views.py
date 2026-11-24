from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import VehiculeForm
from .models import Vehicule


class VehiculeListView(ListView):
    model = Vehicule
    template_name = "vehicule/list.html"
    context_object_name = "vehicules"
    ordering = "-created_at"


class VehiculeCreateView(CreateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = "vehicule/form.html"
    success_url = reverse_lazy("VehiculeApp:list")


class VehiculeUpdateView(UpdateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = "vehicule/form.html"
    success_url = reverse_lazy("VehiculeApp:list")


class VehiculeDeleteView(DeleteView):
    model = Vehicule
    template_name = "vehicule/delete.html"
    success_url = reverse_lazy("VehiculeApp:list")
