
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', include('urls_and_views.core.urls')),


    path("departments/", include("urls_and_views.departments.urls"))
    ]

