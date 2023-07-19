from django.db import models
from django.contrib.auth.models import User


# Create your models here.

precedence_choice = (
    ("primary", "primary"),
    ("secondary", "secondary"),
)
class Contact(models.Model):
    phonenumber = models.TextField(db_index=True)
    email = models.TextField(null=True,blank=True,db_index=True)
    linkedId = models.IntegerField(null=True,blank=True)
    linkprecedence = models.TextField(choices=precedence_choice,default="primary")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return (self.email + " " + self.phonenumber)
    

    