from django.urls import path

from . import views

app_name = "ExpeditionApp"
urlpatterns = [
    path("", views.list_expeditions, name="index"),
    path("home/", views.home, name="home"),
    path("welcome/<str:name>/", views.welcome, name="welcome"),
    path("list/", views.list_expeditions, name="list"),
    path("detail/<int:id>/", views.detail_expedition, name="detail"),
    path(
        "list_expedition/",
        views.Liste_expeditions.as_view(),
        name="liste_classe",
    ),
    path(
        "delete/<int:pk>/",
        views.DeleteExpedition.as_view(),
        name="delete",
    ),
    path(
        "deleteexpedition/<int:pk>/",
        views.DeleteExpedition.as_view(),
        name="delete_expedition",
    ),
    path(
        "create/",
        views.CreateExpedition.as_view(),
        name="create_expedition",
    ),
    path(
        "update/<int:pk>/",
        views.UpdateExpedition.as_view(),
        name="update_expedition",
    ),
]