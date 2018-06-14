from django.db import models
from django.utils import timezone

# Create your models here.
class Request(models.Model):
    requested_by = models.CharField(max_length = 30)
    email = models.EmailField(max_length=254)
    discription = models.TextField()
    logo_type = models.CharField(max_length = 30)
    usage = models.CharField(max_length=30)
    is_created = models.BooleanField(default="False")
    request_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.requested_by

    def completed(self):
        self.is_created = "True"


