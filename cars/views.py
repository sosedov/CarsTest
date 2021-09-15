from rest_framework.views import APIView

class CommonResponseMiddleware (APIView):
    def __init__(self):
        pass

    def process_request(self, request):

        path = request.path_info.lstrip('/')

        method = request.method.upper()

        if method == "DELETE":
            request.META['REQUEST_METHOD'] = 'DELETE'
            request.DELETE = QueryDict(request.body)
        if method == "PUT":
            request.META['REQUEST_METHOD'] = 'PUT'
            request.PUT = QueryDict(request.body)

        params = {}
        if method == "GET":
            params = request.GET.items()
            
        if method == "POST":
            params = request.POST.items()
            
        if method == "PUT":
            params = request.PUT.items()
            
        if method == "DELETE":
            params = request.DELETE.items()
           