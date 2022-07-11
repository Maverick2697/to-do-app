from re import T
from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User


class Task(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length= 50)
    description = models.TextField(max_length=200, null=True, blank=True)
    finished = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        # ordering = ['finished']
        order_with_respect_to = 'user'

