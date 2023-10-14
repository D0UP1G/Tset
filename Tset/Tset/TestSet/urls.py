from django.contrib import admin
from django.urls import path, include
from TestsPage import views as Tests
urlpatterns = [
    path('', include('misc.url')),
    path('admin/', admin.site.urls),
    path("tests/", Tests.index)
]
