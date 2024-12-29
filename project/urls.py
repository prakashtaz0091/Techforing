from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from app.views import LogoutView


urlpatterns = [
    #admin panel
    path('admin/', admin.site.urls),


    #browsable API
    path('api/auth/', include('rest_framework.urls')),  # Optional: browsable API login


    #jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #logout
    path('api/logout/', LogoutView.as_view(), name='logout'),


]

