from django.urls import path
from . import views

urlpatterns = [
    path("api/hello",views.index,name="index"),
]