from .models import Visitor
from django.utils.deprecation import MiddlewareMixin

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        Visitor.objects.create(ip_address=ip_address, user_agent=user_agent)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
