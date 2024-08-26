from django.urls import path
from . import views

app_name = 'home'
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('opera/', views.OperaCreate.as_view(), name='opera-create'),
    path('opera/<int:pk>/', views.OperaDetail.as_view(), name='opera-detail'),
    path('opera/<int:pk>/update/', views.OperaUpdate.as_view(), name='opera-update'),
    path('opera/<int:pk>/delete/', views.OperaDelete.as_view(), name='opera-delete'),
    path('members/', views.MemberCreate.as_view(), name='member-create'),
    path('members/<int:pk>/', views.MemberDetail.as_view(), name='member-detail'),
    path('members/<int:pk>/update/', views.MemberUpdate.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', views.MemberDelete.as_view(), name='member-delete'),
]

