from django.contrib.auth.backends import BaseBackend
from .models import Users


class UsersAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Users.objects.get(username=username)
            if user.check_password(password):
                return user
        except Users.DoesNotExist:
            return None

    def authenticate_header(self, request):
        return 'Bearer'

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None
