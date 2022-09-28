from django.utils.deprecation import MiddlewareMixin


class SetCSRF(MiddlewareMixin):
    @staticmethod
    def process_response(request, response):
        response["X-CSRFToken"] = request.COOKIES.get("csrftoken")
        return response
