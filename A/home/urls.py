from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('opera/', views.opera_list, name='opera-list'),  # To create a new opera (POST request)
    path('opera/<int:pk>/', views.get_opera, name='get-opera'),  # To retrieve a specific opera (GET request)
    path('opera/<int:pk>/update/', views.update_opera, name='update-opera'),  # To update a specific opera (PUT request)
    path('opera/<int:pk>/delete/', views.delete_opera, name='delete-opera'),  # To delete a specific opera (DELETE request)
    path('members/', views.create_member, name='create-member'),  # To create a new member (POST request)
    path('members/<int:pk>/', views.get_member, name='get-member'),
    path('members/<int:pk>/update/', views.update_member, name='update-member'),
    path('members/<int:pk>/delete/', views.delete_member, name='delete-member'),
]
