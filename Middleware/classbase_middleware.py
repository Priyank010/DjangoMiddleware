from typing import Any

class DemoMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request, *args: Any, **kwds: Any) -> Any:
        
        response = self.get_response(request)
        print("Class based Middleware")

        return response
    
    def process_view(request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        pass

    def process_exception(request, exception):
        # This code is executed if an exception is raised
        pass

    def process_template_response(request, response):
        # This code is executed if the response contains a render() method
        return response