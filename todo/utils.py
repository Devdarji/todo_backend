from rest_framework.response import Response


def create_response(data, code, message=None, extra=None):
    if not message:
        if code == 400:
            message = "Bad request"
        elif code == 200:
            message = "Success"

    return Response(
        data={"data": data, "message": message, "code": code, "extra": extra},
        status=code,
    )
