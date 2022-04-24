from django.urls import path, include
from .views import registrazioneView

urlpatterns = [
    path('registrazione/', registrazioneView, name='registrationView'),
]