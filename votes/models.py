from django.db import models
from django.contrib import admin

# add models here
class Link(models.Model):
    CATEGORIES = [
        ("r", "Restaurant"),
        ("e", "Emails"),
        ("d", "Donate"),
        ("s", "Source"),
        ("m", "Memorials"),
        ("l", "Learn"),
    ]
    type = models.CharField(max_length=1, choices=CATEGORIES) 
    state = models.CharField(max_length=2)
    url = models.CharField(max_length=300)
    text = models.CharField(max_length=100)
    def __str__(self):
        return self.text

class LinkAdmin(admin.ModelAdmin):
    list_filter = ("type", "state")
    list_display = ("text", "type", "state")

class Message(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text