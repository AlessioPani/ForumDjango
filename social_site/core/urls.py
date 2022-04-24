from django.urls import path
from .views import HomeView, userProfileView, userListView, cerca

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('user/<username>/', userProfileView, name='user_profile'),
    path('users/', userListView.as_view(), name='user_list'),
    path('cerca/', cerca, name='funzione_cerca')
]
