from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView , UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from ExpeditionApp.forms import ExpeditionForm
from django.urls import reverse_lazy
from .models import Expedition


def home(request):
    return HttpResponse("<h1>Bienvenue sur l'application ExpeditionApp !</h1>")


def welcome(request, name):
    return HttpResponse(f"Bienvenue, {name} !")


def list_expeditions(request):
    expeditions = Expedition.objects.filter(status="p").order_by("created_at")
    return render(
        request,
        "expedition/list.html",
        {"expeditions": expeditions},
    )


def detail_expedition(request, id):
    expedition = get_object_or_404(Expedition, id=id)
    return render(
        request,
        "expedition/detail.html",
        {"expedition": expedition},
    )

class DetailExpedition(DetailView):
    model = Expedition
    template_name = "expedition/detail.html"
    context_object_name = "expedition"

class Liste_expeditions(ListView):
    model = Expedition
    template_name = "expedition/list.html"
    context_object_name = "expeditions"
    queryset = Expedition.objects.filter(status="p").order_by("created_at")

class DeleteExpedition(DeleteView):
    model = Expedition
    template_name = "expedition/delete.html"
    success_url = reverse_lazy("ExpeditionApp:liste_classe")


class CreateExpedition(CreateView):
    model = Expedition
    template_name = "expedition/forms.html"
    #fields = "__all__"
    form_class = ExpeditionForm
    success_url = reverse_lazy("ExpeditionApp:liste_classe")

class UpdateExpedition(UpdateView):
    model = Expedition
    template_name = "expedition/forms.html"
    form_class = ExpeditionForm
    success_url = reverse_lazy("ExpeditionApp:liste_classe")