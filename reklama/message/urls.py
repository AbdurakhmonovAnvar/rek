from django.urls import path
from .views import MessageGetView, MessageDeleteView, MessageCreateView, MessageUpdateView

urlpatterns = [
    path('message/', MessageGetView.as_view(), name='message-get'),  # message list
    path('message/<int:pk>/', MessageDeleteView.as_view(), name='message-delete'),  # delete
    path('message_create/', MessageCreateView.as_view(), name='message-create'),  # message post
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message-update'),  # update
]
