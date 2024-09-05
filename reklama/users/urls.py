from django.urls import path
from .views import UserGetView, CustomTokenObtainView, UpdateUserView, DeleteUserView, UserRegisterView, \
    UserRegisterTelView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('get_token/', CustomTokenObtainView.as_view(), name='token'),  # token (login)
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # access_tokenni yangilash
    path('user/', UserGetView.as_view(), name='user-get'),
    path('user/update/', UpdateUserView.as_view(), name='user-update'),
    path('user/delete/', DeleteUserView.as_view(), name='user-delete'),
    path('user/create/', UserRegisterView.as_view(), name='user-create'),
    path('user/create/tel/', UserRegisterTelView.as_view(), name='user-create-tel'),  # tel raqam bn registr
]
