from django.shortcuts import render
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from .models import Message
from rest_framework.permissions import IsAuthenticated
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework import status


class MessageGetView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return Message.objects.filter(user_id=user.id)


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MessageDeleteView(DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        message_id = kwargs.get('pk')
        user = request.user
        message = Message.objects.filter(id=message_id, user_id=user.id)
        if not message:
            return Response({'message': "Bunday message bu userga tegishli emas"})
        message.delete()
        return Response({'message': "Bu message o'chirildi"})


class MessageUpdateView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        message_id = kwargs.get('pk')
        user = request.user
        message = Message.objects.filter(id=message_id, user=user)
        if not message:
            return Response({'message': "Bunday message yoq yoki bu userga tegishli emas"})
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': "O'zgartirildi"})


def msg(request):
    return render(request, 'message.html')
