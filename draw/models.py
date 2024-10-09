from django.db import models

class UserR(models.Model):
    name=models.CharField(max_length=5)
    password=models.CharField(max_length=7)
class Design(models.Model):
    user = models.ForeignKey(UserR, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    data = models.TextField()  # Store drawing data as JSON or another format
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
