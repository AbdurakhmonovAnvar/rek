from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Users


class UserSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    # user_id = serializers.Field(required=False)
    # phone_number = serializers.Field(required=False)
    # status = serializers.Field(required=False)
    # language = serializers.Field(required=False)
    # image_path = serializers.Field(required=False)
    # tg_status = serializers.Field(required=False)

    class Meta:
        model = Users
        fields = ['user_id', 'username', 'password', 'phone_number', 'status', 'language', 'image_path', 'email',
                  'tg_status', 'created_at', 'image']


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    phone_number = serializers.CharField(required=False, allow_blank=True)
    email = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Users
        fields = ['user_id', 'username', 'password', 'status', 'email', 'phone_number']


class UserToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['phone_number'] = user.phone_number
        token['password'] = user.password
        token['status'] = user.status

        return token

    def validate(self, attrs):
        username_or_phone = attrs.get('username') or attrs.get('phone_number')
        password = attrs.get('password')

        if not username_or_phone or not password:
            raise AuthenticationFailed('Username or phone number and password are required')

        user = Users.objects.filter(username=username_or_phone).first() or \
               Users.objects.filter(phone_number=username_or_phone).first()

        if user is None:
            raise AuthenticationFailed('No user found with this username or phone number')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        return super().validate({
            'username': user.username,
            'password': password,
        })
