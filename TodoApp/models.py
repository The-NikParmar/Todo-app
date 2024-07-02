from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    des = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.name + self.des
