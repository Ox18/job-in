from django.http import JsonResponse

class Response:
    @staticmethod
    def ok(data, message):
        return JsonResponse({
            'status': 'success',
            'data': data,
            'message': message
        })