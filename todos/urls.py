from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("create_todo/", views.create_todo, name="create_todo"),
    path("delete_todo/<int:id>", views.delete_todo, name="delete_todo"),
    path("update_todo/<int:id>", views.update_todo, name="update_todo"),
    path("toggle/<int:pk>/", views.toggle_todo, name="toggle_todo")
]