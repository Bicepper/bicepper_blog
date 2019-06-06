from django.contrib import admin
from .models import BlogPost
from .models import Category
# from .models import SubCategory

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Category)
# admin.site.register(SubCategory)