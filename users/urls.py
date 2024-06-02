from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserDetailAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path('', UserListAPIView.as_view(), name='users_list'),
    path('create/', UserCreateAPIView.as_view(), name='users_create'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='users_detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='users_delete'),
]
