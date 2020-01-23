from django.http import HttpResponse, Http404
from .models import BlogPost


def ip_restriction(request, *args, **kwargs):
    pass


def blog_detail_admin_only(func):
    def check_admin(request, *args, **kwargs):
        check_limit = BlogPost.objects.filter(pk=kwargs['pk']).values('is_public', 'is_author')
        if not check_limit:
            raise Http404

        if check_limit[0]['is_author'] is True or check_limit[0]['is_public'] is False:
            if request.user.is_authenticated:
                pass
            else:
                raise Http404
        return func(request, *args, **kwargs)
    return check_admin
