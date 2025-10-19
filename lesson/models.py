from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=15, choices=[("admin", "user")])

    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=100)
    description =  models.TextField()
    status = models.CharField(max_length=20, choices=[
        ("in progress", "In progress"),
        ("completed", "Completed"),
        ("postponed", "Postponed"), 
    
    ], default="in progress"
    )
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=True)

def __str__(self):
    return f"{self.title} - {self.status}"