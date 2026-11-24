from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import EntrepriseForm, RegistrationForm
from .models import Entreprise


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("ExpeditionApp:index")
    else:
        form = RegistrationForm()
    return render(request, "offre/register.html", {"form": form})


class EntrepriseListView(ListView):
    model = Entreprise
    template_name = "entreprise/list.html"
    context_object_name = "entreprises"
    ordering = "-created_at"


class EntrepriseCreateView(CreateView):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = "entreprise/form.html"
    success_url = reverse_lazy("EntrepriseApp:list")


class EntrepriseUpdateView(UpdateView):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = "entreprise/form.html"
    success_url = reverse_lazy("EntrepriseApp:list")


class EntrepriseDeleteView(DeleteView):
    model = Entreprise
    template_name = "entreprise/delete.html"
    success_url = reverse_lazy("EntrepriseApp:list")
