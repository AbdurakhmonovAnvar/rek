from django.urls import path
from .views import MessageGetView, MessageDeleteView, MessageCreateView, MessageUpdateView
from . import views

urlpatterns = [
    path('api/v1/message/', MessageGetView.as_view(), name='message-get'),  # message list
    path('api/v1/message/<int:pk>/', MessageDeleteView.as_view(), name='message-delete'),  # delete
    path('api/v1/message_create/', MessageCreateView.as_view(), name='message-create'),  # message post
    path('api/v1/message_update/<int:pk>/', MessageUpdateView.as_view(), name='message-update'),  # update
    # path('msg/', views.msg, name='msg'),  # update

]
