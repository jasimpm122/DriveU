from django.urls import path

from website.views import home, index, some_json, blr, drive_u
from . import views

urlpatterns = [
    path("blog", home),
    path("some-text/", index),
    path("some-json/", some_json),
    path("bangalore/", blr),
    path("driveu/", drive_u),

]
