from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class StopMotion(models.Model):
    """
    Stop motion Model
    """
    video = models.URLField(max_length=1024, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')