
from django.contrib import admin
from django.urls import path, include
# from django.urls import include

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]
