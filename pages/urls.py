from django.urls import path
from .views import HotSpotsView, ContactView,HomeView,TicketView

urlpatterns = [
    path("hotspots/", HotSpotsView.as_view(), name="Hot Spots"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("tickets/", TicketView.as_view(), name="tickets"),
]