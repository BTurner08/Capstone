from django.shortcuts import render
from django.views import View

class HotSpotsView(View):
    template_name = "pages/hotspots.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    

class ContactView(View):
    template_name = "pages/contact.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
class HomeView(View):
    template_name = "pages/home.html"
    
    def get(self, request):
        return render(request, self.template_name)
        
