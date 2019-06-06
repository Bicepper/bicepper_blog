from django.contrib import admin
from .models import BlogPost
from .models import ParentCategory
from .models import SubCategory

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(ParentCategory)
admin.site.register(SubCategory)