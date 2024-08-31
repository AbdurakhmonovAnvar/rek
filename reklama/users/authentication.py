from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import Token

from .models import Users


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            # Token orqali Person modelidan foydalanuvchini olish
            user_id = validated_token['user_id']
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            raise AuthenticationFailed('Person not found', code='user_not_found')

        if not user.is_active:
            raise AuthenticationFailed('Person is inactive', code='user_inactive')

        return user
