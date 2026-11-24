from django.urls import path
from . import views

app_name = "OffreApp"

urlpatterns = [
    path("", views.OffreListView.as_view(), name="list"),
    path("create/", views.OffreCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.OffreUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.OffreDeleteView.as_view(), name="delete"),
]
