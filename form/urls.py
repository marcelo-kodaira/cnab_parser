from django.urls import path
from .views import CNABView

urlpatterns = [
    path('form/', CNABView.as_view(), name='cnab'),
]