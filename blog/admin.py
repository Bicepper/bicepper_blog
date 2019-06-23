from django.contrib import admin
from .models import BlogPost
from .models import ParentCategory
from .models import SubCategory
from .models import Profile
from .models import PrivacyPolicy
from .models import GoogleAnalytics

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(ParentCategory)
admin.site.register(SubCategory)
admin.site.register(Profile)
admin.site.register(PrivacyPolicy)
admin.site.register(GoogleAnalytics)

