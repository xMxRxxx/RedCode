from django.contrib import admin
from .models import BlogModel, BlogProjectModel
# Register your models here.
admin.site.register(BlogModel)
admin.site.register(BlogProjectModel)