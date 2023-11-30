from django.urls import path

from . import views

app_name = "contact"
urlpatterns = [
#     # ex: /polls/
    path("", views.index, name="index"),
    # path("", views.IndexView.as_view(), name="index"),
    # path("", views.vote, name="vote"),
]