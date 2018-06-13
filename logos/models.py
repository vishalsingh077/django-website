from django.db import models
from django.utils import timezone

# Create your models here.
class Logo(models.Model):
    logo_img = models.FileField(default = "None")
    logo_name = models.CharField(max_length = 30)
    logo_type = models.CharField(max_length = 30)
    software_used = models.CharField(max_length = 100, blank = "True")
    requested_by = models.CharField(max_length = 30, blank = "True")
    created_by = models.CharField(max_length = 30)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.logo_name
    
                                       
