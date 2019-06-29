from django.http import HttpResponse
from django.template.loader import get_template

from bicepper_blog.settings import production


class IpRestrictMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META['REMOTE_ADDR']

        if ip not in production.ALLOWED_IP_BLOCKS or ip in production.DENY_IP_BLOCKS:
            temp = get_template('not_allowed_ip.html')
            result = temp.render({'ip': ip})
            return HttpResponse(result)
        else:
            response = self.get_response(request)

        return response

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass
