from django.contrib import admin
from .models import *

# register models here
admin.site.register(Link, LinkAdmin)
admin.site.register(Message)