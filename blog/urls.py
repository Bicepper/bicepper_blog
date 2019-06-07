from django.urls import path
from .views import (
    PostList,
    CategoryList,
    SubCategoryList,
)

app_name = 'blog'
urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('category/<str:category>', CategoryList.as_view(), name='category_list'),
    path('category/<str:category__parent__slug>/<str:category__slug>', SubCategoryList.as_view(),
         name='sub_category_list'),
]