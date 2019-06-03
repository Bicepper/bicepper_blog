from django.contrib import admin
from .models import BlogPost
from .models import Category

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Category)