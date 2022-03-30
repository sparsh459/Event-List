from multiprocessing import Event
from django.db import models

# Create your models here.
class events(models.Model):
    Category_choice = (
        ('Family','Family'),
        ('18+','18+'),
        ('Comedy Show','Comedy Show'),
        ('Children Show','Children Show'),
    )
    Name = models.CharField(max_length=250)
    City = models.CharField(max_length=250)
    Category = models.CharField(max_length=250, choices=Category_choice)
    Date = models.DateField(blank=False)
    Price = models.IntegerField(blank=False)

    def __str__(self) -> str:
        return self.EventName
    