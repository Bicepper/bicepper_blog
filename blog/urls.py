from django.urls import path
from .views import (
    PostList,
    CategoryList,
)

app_name = 'blog'
urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('category/<str:category>', CategoryList.as_view(), name='category_list'),
]