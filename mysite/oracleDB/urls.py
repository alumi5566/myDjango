from django.urls import path

from . import views

app_name = "oracleDB"
urlpatterns = [
#     # ex: /oracleDB/
    path("", views.index, name="index"),
]