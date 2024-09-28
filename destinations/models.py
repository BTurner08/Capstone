from django.db import models



class Destinations(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()   
    price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    

class DestinationImage(models.Model):
    post = models.ForeignKey(Destinations, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="images/destinations", blank=True, null=True)
    
    def __str__(self) -> str:
        return self.post.title
    
