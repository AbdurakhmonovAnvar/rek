from django.urls import path
from .views import UserGetView, CustomTokenObtainView, UpdateUserView, DeleteUserView, UserRegisterView, \
    UserRegisterTelView,LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('api/v1/get_token/', CustomTokenObtainView.as_view(), name='token'),  # token (login)
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # access_tokenni yangilash
    path('api/v1/user/', UserGetView.as_view(), name='user-get'),
    path('api/v1/user/update/', UpdateUserView.as_view(), name='user-update'),
    path('api/v1/user/delete/', DeleteUserView.as_view(), name='user-delete'),
    path('api/v1/user/create/', UserRegisterView.as_view(), name='user-create'),
    path('api/v1/user/create/tel/', UserRegisterTelView.as_view(), name='user-create-tel'),  # tel raqam bn registr
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', views.user, name='user-view'),
    path('login/', views.login, name='user-login'),
    path('register/', views.register, name='user-login'),
    path('post/', views.post_adver, name='user-post'),
    path('my_ads/', views.my_ads, name='user-my-ads'),
]
