from django.contrib import admin
from .models import BlogPost
from .models import ParentCategory
from .models import SubCategory
from .models import Profile
from .models import PrivacyPolicy
from .models import GoogleAnalytics
from .models import PopularPost
from .models import SideBanner1


# Register your models here.
admin.site.register(BlogPost)
admin.site.register(ParentCategory)
admin.site.register(SubCategory)
admin.site.register(Profile)
admin.site.register(PrivacyPolicy)
admin.site.register(GoogleAnalytics)
admin.site.register(PopularPost)
admin.site.register(SideBanner1)


