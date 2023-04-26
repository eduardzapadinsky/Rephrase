"""
URL configuration for rephrase_api app.
"""

from django.urls import path

from . import views

app_name = "rephrase-api"
urlpatterns = [
    path("paraphrase", views.ParaphraseAPIView.as_view(), name="paraphrase"),
]
