class SessionHeaderMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.process_request(request)

    def process_request(self, request):
        session_uuid = request.META.get('HTTP_SESSION', '')
        setattr(request, 'session_uuid', session_uuid)
        response = self.get_response(request)
        return response
