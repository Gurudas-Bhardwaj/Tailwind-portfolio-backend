from django.db import models


class ContactModel(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=60)
    Number=models.IntegerField(default=10)
    Subject=models.CharField(max_length=100)
    Message=models.TextField(default="empty")