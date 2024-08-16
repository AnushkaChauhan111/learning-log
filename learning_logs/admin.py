from django.contrib import admin

# Register your models here.
from .models import Topic #(.models to ask it to find models in same directory as admin)
admin.site.register(Topic)