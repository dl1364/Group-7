from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('userpage/', include('userpage.urls')),
    path('admin/', admin.site.urls),
]