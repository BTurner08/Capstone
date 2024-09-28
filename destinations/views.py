from typing import Any
from django.db.models.query import QuerySet
from django. shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Destinations

# Create your views here.
def home(request) :
    return render(request, "destinations/home.html")

class DestinationsListPage(ListView):
    model=Destinations
    template_name = "destinations/list.html"
    context_object_name = "destinations"
    
    def get_queryset(self):
        return Destinations.objects.prefetch_related('images').all()        
    
    
    
class DestinationsDetailsPage(DetailView):
    model = Destinations
    template_name = "destinations/details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_destinations'] = Destinations.objects.all()
        return context
    
class TicketsDetailsPage(DetailView):
    model = Destinations
    template_name = "destinations/tickets.html"
    context_object_name = 'destination'