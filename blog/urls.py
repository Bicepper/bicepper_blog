from django.urls import path
from .decorators import blog_detail_admin_only
from .views import (
    PostList,
    CategoryList,
    SubCategoryList,
    ArchiveList,
    PostDetailView,
    ProfileView,
)

app_name = 'blog'
urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('category/<str:category>', CategoryList.as_view(), name='category_list'),
    path('category/<str:category__parent__slug>/<str:category__slug>', SubCategoryList.as_view(),
         name='sub_category_list'),
    path('<int:year>/<int:month>', ArchiveList.as_view(), name='archive_list'),
    path('detail/<int:pk>', blog_detail_admin_only(PostDetailView.as_view()), name='detail'),
    path('profile', ProfileView.as_view(), name='profile'),
]