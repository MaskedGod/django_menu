from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("about/team/", views.team, name="team"),
    path("services/", views.service, name="services"),
    path("services/web/", views.web, name="web_dev"),
    path("services/seo/", views.seo, name="seo"),
    path("contact/", views.contact, name="contact"),
]
