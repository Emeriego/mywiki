from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("dynamo2", views.dynamo2, name="check"),
    # path("<str:customtext>", views.dynamo, name="dynamo"),
    # path("me", views.me, name="me"),

]
