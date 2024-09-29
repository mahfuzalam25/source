from django.db import models

from django.core.exceptions import ValidationError
import os

# Custom validator for image file extensions
def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # Extract the file extension
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {ext}. Allowed extensions are: .jpg, .jpeg, .png, .webp, .svg')
# Create your models here.

class Home(models.Model):
    intro = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='adminimg/', validators=[validate_image_extension])

    def __str__(self):
        return self.name + "'s updated dashboard"

class Portfolio(models.Model):
    image = models.FileField(upload_to='portfolio/', validators=[validate_image_extension])
    link = models.URLField(max_length=200)
    def __str__(self):
        return "Updated portfolio!"

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + " - " + self.email

