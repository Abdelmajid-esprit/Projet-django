from django.urls import path
from . import views

app_name = "EntrepriseApp"

urlpatterns = [
    path("", views.EntrepriseListView.as_view(), name="list"),
    path("create/", views.EntrepriseCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.EntrepriseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.EntrepriseDeleteView.as_view(), name="delete"),
]
