from django.contrib import admin
from django.urls import include
from django.urls import path
from api.router import router
from api.views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login')
]
