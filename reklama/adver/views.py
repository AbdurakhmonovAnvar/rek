import shutil
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from .serializers import AdverSerializer
from .models import Adver, Street, Adver_type
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
import string
import random
import os


class AdverGetView(ListAPIView):
    queryset = Adver.objects.all()
    serializer_class = AdverSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return Adver.objects.filter(user=user)


class AdverCreateView(APIView):
    queryset = Adver.objects.all()
    serializer_class = AdverSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        print(request.data)
        title = request.data.get('title')
        content = request.data.get('content')
        address = request.data.get('address')
        contact = request.data.get('contact')
        price = request.data.get('price')
        street_id = request.data.get('street')
        type_id = request.data.get('type')
        images = request.data.getlist('image', None)
        user_id = user.id

        street = get_object_or_404(Street, id=street_id)
        adver_type = get_object_or_404(Adver_type, id=type_id)
        location = f"d:\\image\\{user.user_id}\\{generate_random_string(5)}"
        adver = Adver(title=title,
                      content=content,
                      address=address,
                      contact=contact,
                      status='deactice',
                      price=price,
                      street=street,
                      type=adver_type,
                      user=user,
                      image_url=location)

        if images:
            if not os.path.exists(location):
                os.makedirs(location)
            for image in images:
                fs = FileSystemStorage(location=location)
                fs.save(image.name, image)
        adver.save()
        return Response({'message': "Ma'lumotlar qabul qilindi"}, status=status.HTTP_200_OK)


class AdverUpdateView(APIView):
    queryset = Adver.objects.all()
    serializer_class = AdverSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        adver = Adver.objects.filter(user=user, id=kwargs.get('pk')).first()
        if not adver:
            return Response({'message': "Bunday adver userga tegishli emas"})
        title = request.data.get('title', adver.title)
        content = request.data.get('content', adver.content)
        address = request.data.get('address', adver.address)
        contact = request.data.get('contact', adver.contact)
        price = request.data.get('price', adver.price)
        street_id = request.data.get('street', adver.street)
        type_id = request.data.get('type', adver.type)
        images = request.FILES.getlist('image', None)

        street = get_object_or_404(Street, id=street_id)
        adver_type = get_object_or_404(Adver_type, id=type_id)

        adver.title = title
        adver.content = content
        adver.address = address
        adver.contact = contact
        adver.price = price
        adver.adver_type = adver_type
        adver.street = street

        if images:
            location = adver.image_url
            if os.path.exists(location):
                for item in os.listdir(location):
                    os.remove(f"{location}\\{item}")
            for image in images:
                fs = FileSystemStorage(location=location)
                fs.save(image.name, image)
        adver.save()
        return Response({'message': "Updated"})


class AdverDeleteView(DestroyAPIView):
    queryset = Adver.objects.all()
    serializer_class = AdverSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        adver_id = kwargs.get('pk')
        adver = Adver.objects.filter(user=user, id=adver_id).first()
        image_path = adver.image_url
        if os.path.exists(image_path):
            shutil.rmtree(image_path)
        adver.delete()
        return Response({'message': "Content o'chirildi"}, status=status.HTTP_204_NO_CONTENT)





def generate_random_string(length):
    letters = string.ascii_lowercase  # Kichik harflarni tanlash
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string
