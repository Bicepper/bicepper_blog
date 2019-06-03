from django.shortcuts import render
from django.views.generic import View
from .models import BlogPost


class PostList(View):
    @staticmethod
    def get(request, *args, **kwargs):
        post_list = BlogPost.objects.all()
        print(post_list)
        context = {
            'post_list': post_list,
        }
        return render(request, 'blog/post_list.html', context)



