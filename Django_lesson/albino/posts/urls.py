from django.urls import path

# from albino import views
from . import views

urlpatterns = [
    path("", views.posts_list),
]