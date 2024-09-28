from django.urls import path
from .views import home, DestinationsDetailsPage, DestinationsListPage,TicketsDetailsPage

urlpatterns = [
path('', home, name="destinations_home"),
path ('list/', DestinationsListPage.as_view(), name="list"),
path('details/<int:pk>/', DestinationsDetailsPage.as_view(), name="destination_details"),
path('details/<int:pk>/tickets/', TicketsDetailsPage.as_view(), name="destination_tickets"),
]