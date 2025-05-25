from django.urls import path
from .views import RentSearchFilterView

urlpatterns = [
    path('', RentSearchFilterView.as_view(), name='rent-search-filter'),
]
