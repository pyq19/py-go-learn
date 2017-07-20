from functools import wraps


def convert_exception_to_response(get_response):
    @wraps(get_response)  #, assigned= TODO
    def inner(request):
        try:
            response = get_response(request)
        except Exception as exc:
            response = response_for_exception(request, exc)
        return response
    return inner


# TODO
def response_for_exception(request, exc):
    response = None
    return response
