from .models import UserActivity

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            UserActivity.objects.create(user=request.user, path=request.path[1:])
        response = self.get_response(request)
        return response