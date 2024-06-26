from django.db import models
import torch
import pandas
# Create your models here.

def upload_image(object, filename):
    return f'{object.created_at}--{filename}'


class ImageDetection(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='teste', blank=False, null=True)
    model_evaluation = models.JSONField(default=list, blank=True, null=True)

    
