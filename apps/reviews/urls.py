from django.urls import path
from views import ReviewCreateView

urlpatterns = [
    path('reviews/create/', ReviewCreateView.as_view(), name='create-review'),
]
