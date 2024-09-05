from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserToken
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Users
from .serializers import UserSerializers, UserCreateSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.files.storage import FileSystemStorage
import os


class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = UserToken


class UserGetView(APIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializers = UserSerializers(user)
        return Response(serializers.data, status=status.HTTP_200_OK)


class UpdateUserView(APIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        print(user)
        if user is None:
            return Response({'message': "Bunday foydalnauvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        user_id = request.data.get('user_id', user.user_id)
        username = request.data.get('username', user.username)
        password = request.data.get('password', user.password)
        phone_number = request.data.get('phone_number', user.phone_number)
        language = request.data.get('language', user.language)
        email = request.data.get('email', user.email)
        images = request.FILES.getlist('image', user.image_path)
        user.user_id = user_id
        user.username = username
        user.password = password
        user.phone_number = phone_number
        user.language = language
        user.email = email
        if images:
            location = f"d:\\image\\{user.user_id}\\image"
            if not os.path.exists(location):
                os.makedirs(location)
            if len(images) > 1:
                return Response({'message': "Rasmlar soni ko'p"})
            fs = FileSystemStorage(location=location)
            fs.save(images[0].name, images[0])
            user.image_path = location
        user.save()
        return Response({'message': "O'zgartirildi"}, status=status.HTTP_200_OK)


class DeleteUserView(APIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        user.status = 'deactive'
        user.username = ''
        user.password = ''
        user.email = ''
        user.language = ''
        user.save()
        return Response({'message': "User deactivlantirildi"})


class UserRegisterView(APIView):
    queryset = Users.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def post(self, requst, *args, **kwargs):
        username = requst.data.get('username', '')
        password = requst.data.get('password', '')
        phone_number = requst.data.get('phone_number', '')
        email = requst.data.get('email', '')
        if Users.objects.filter(username=username):  # or Users.objects.filter(email=email):
            return Response({'message': "Bunday user tizimda mavjud "}, status=status.HTTP_400_BAD_REQUEST)
        if not [username, password, email]:
            return Response({'message': "Kerakli fieldlar mavjud emas"}, status=status.HTTP_400_BAD_REQUEST)

        user_data = {
            'username': username,
            'password': password,
            'phone_number': '+998',
            'email': '',
            'status': 'active',
            'user_id': 0
        }
        serializers = UserCreateSerializer(data=user_data)
        if serializers.is_valid():
            user = serializers.save()
            return Response({
                'message': 'User created successfully',
                'user': UserCreateSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterTelView(APIView):
    queryset = Users.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def post(self, requst, *args, **kwargs):
        # username = requst.data.get('username', '')
        password = requst.data.get('password', '')
        phone_number = requst.data.get('phone_number', '')
        # email = requst.data.get('email', '')
        if Users.objects.filter(phone_number=phone_number):  # or Users.objects.filter(email=email):
            return Response({'message': "Bunday user tizimda mavjud "})
        if not [phone_number, password]:
            return Response({'message': "Kerakli fieldlar mavjud emas"}, status=status.HTTP_400_BAD_REQUEST)

        user_data = {
            'username': f'u{str(phone_number).replace("+", "")}',
            'phone_number': phone_number,
            'password': password,
            'email': '',
            'status': 'active',
            'user_id': 0
        }
        serializers = UserCreateSerializer(data=user_data)
        if serializers.is_valid():
            user = serializers.save()
            return Response({
                'message': 'User created successfully',
                'user': UserCreateSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
