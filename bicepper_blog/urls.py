"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from bicepper_blog.settings import production
from django.conf.urls.static import static
from filebrowser.sites import site

from blog .views import (
    ContactView,
    ContactResultView,
    PrivacyPolicyView,
)

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('bicepper_chicken_leg/', admin.site.urls),
    path('', include('blog.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('contact', ContactView.as_view(), name='contact'),
    path('contact/result', ContactResultView.as_view(), name='contact_result'),
    path('privacy', PrivacyPolicyView.as_view(), name='privacypolicy'),
]

urlpatterns += static(production.MEDIA_URL, document_root=production.MEDIA_ROOT)
