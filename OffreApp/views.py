from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import OffreForm
from .models import Offre


class OffreListView(ListView):
    model = Offre
    template_name = "offre/list.html"
    context_object_name = "offres"
    ordering = "-created_at"


class OffreCreateView(CreateView):
    model = Offre
    form_class = OffreForm
    template_name = "offre/form.html"
    success_url = reverse_lazy("OffreApp:list")


class OffreUpdateView(UpdateView):
    model = Offre
    form_class = OffreForm
    template_name = "offre/form.html"
    success_url = reverse_lazy("OffreApp:list")


class OffreDeleteView(DeleteView):
    model = Offre
    template_name = "offre/delete.html"
    success_url = reverse_lazy("OffreApp:list")
