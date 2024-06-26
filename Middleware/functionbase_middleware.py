def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)
        print("Function Based Middleware")

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware