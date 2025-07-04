# myapp/middleware.py

from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        
        print("Request Middleware Active")
        return None

    def process_response(self, request, response):
        print("🟢 Response Middleware Active")
        return response
