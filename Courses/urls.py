from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_course, name='create-course'),
    path('search/', views.retrieve_course, name='retrieve-course'),
    path('update/<int:pk>', views.update_course, name='update-course'),
    path('delete/<int:pk>', views.delete_course, name='delete-course'),
]