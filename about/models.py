from django.db import models
from cloudinary.models import CloudinaryField
# from django.contrib.auth.models import User
# Create your models here.


class About(models.Model):
    """
    Stores a slingle about me text.
    """
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a slingle collaboration request message.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
