from django.db import models

# Create your models here.

class Math(models.Model):
    operation = models.CharField(max_length=10)
    a = models.IntegerField()
    b = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.operation} {self.a} {self.b}"
