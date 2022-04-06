from django.contrib import admin
from django.urls import path, include

#Rotas para os Cursos
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Courses.urls')),
]
