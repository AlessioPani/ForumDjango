from django.urls import path
from . import views

urlpatterns = [
    path(
        'nuova-sezione/',
        views.CreaSezioneView.as_view(),
        name="crea_sezione"),
    path(
        'sezione/<int:pk>',
        views.visualizza_sezione,
        name="sezione_view"),
    path(
        'sezione/<int:pk>/crea-discussione/',
        views.creaDiscussione,
        name="crea_discussione"),
    path(
        'discussione/<int:pk>',
        views.visualizzaDiscussione,
        name="visualizza_discussione"),
    path(
        'discussione/<int:pk>/rispondi',
        views.aggiungiRisposta,
        name="rispondi_a_discussione"),
    path(
        'discussione/<int:id>/elimina_post/<int:pk>',
        views.CancellaPost.as_view(),
        name="cancella_post"),
]
