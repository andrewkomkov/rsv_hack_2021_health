from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('life_checker_app/', include('life_checker_app.urls')),
    path('admin/', admin.site.urls),
]