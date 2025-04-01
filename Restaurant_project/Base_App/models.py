from django.db import models
from django.utils.translation import gettext_lazy as _  # Translation support

from django.db import models

class ItemList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):  # Fixed indentation
        return self.name



class Items(models.Model):
    name = models.CharField(max_length=255, default="Default Item Name")
    description = models.TextField(default="No description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.ForeignKey(ItemList, related_name='items', on_delete=models.CASCADE, default=1)  # Set default to a valid category ID
    image = models.ImageField(upload_to='uploads/', default='uploads/default.jpg')

    def __str__(self):
        return self.name




class AboutUs(models.Model):
    description = models.TextField(default="No description")

    def __str__(self):
        return self.description  # Or any other relevant field



from django.core.validators import MaxValueValidator, MinValueValidator

from django.core.validators import MaxValueValidator, MinValueValidator

class Feedback(models.Model):
    user_name = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], 
        default=3  # Set a default value
    )

    def __str__(self):
        return self.user_name



class BookTable(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
